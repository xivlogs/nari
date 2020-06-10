#!/usr/bin/env python3.8
"""Entrypoint into the base nari cli client"""

from argparse import ArgumentParser, Namespace
from logging import basicConfig, getLogger, Logger, CRITICAL, INFO
from typing import List, cast

from nari.io.actlog import ActLogReader
from nari.io.reader import Reader
from nari.parser.normaliser import Normaliser
from nari.types.event import Type as EventType
from nari.types.event.directorupdate import DirectorUpdateCommand, DirectorUpdate

DEFAULT_LOG_FORMAT: str = '[%(levelname)s] %(message)s'
logger: Logger = getLogger('nari')


def print_matrix(matrix: List[List[str]]):
    """Hacky function to print out an 'aligned' set of data"""
    col_width = max(len(word) for row in matrix for word in row) + 2
    for row in matrix:
        print(''.join(word.ljust(col_width) for word in row))



def parse_fights(reader: Reader) -> List[List[str]]:
    """Takes in a reader object and parses the fight details out of it"""
    class DirectorFilter(Normaliser):
        """Literally only filters out director updates"""
        def on_event(self, event):
            if event.id == EventType.directorupdate:
                return event
            return None

    fight_log: List[dict] = []
    current_fight: dict = {}

    for event in DirectorFilter(reader):
        command = event.director_command # type: ignore
        if command == DirectorUpdateCommand.init:
            if current_fight:
                fight_log.append(current_fight)
            current_fight = {
                'date': event.timestamp,
                'name': str(event.instance_id), # type: ignore
            }
        elif command in (DirectorUpdateCommand.fadeout, DirectorUpdateCommand.clear): # naive, but functional?
            current_fight['fights'] = current_fight.get('fights', 0) + 1

    column_headers = ['date', 'instance id', 'encounters']
    matrix = [column_headers]

    for fight in fight_log:
        num_fights = fight.get('fights', 0)
        amtstr = 'fight' if num_fights == 1 else 'fights'
        matrix.append([
            f'[{fight["date"]}]',
            fight['name'],
            f'{num_fights} {amtstr}',
        ])

    return matrix


def create_parser() -> ArgumentParser:
    """Convienience function to create the argument parser"""
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument('log', help='Path to an ACT .log file')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-e', '--error', action='store_true', help='Raises an exception on an unknown event ID')

    return parser


def handle_args(log=None, verbose=False, error=False) -> None:
    """Just runs what we've got"""
    if verbose:
        basicConfig(format=DEFAULT_LOG_FORMAT, level=INFO)
    else:
        basicConfig(format=DEFAULT_LOG_FORMAT, level=CRITICAL)

    # We only really do ACT Network logs for now, so no need to do fancy file detection or anything like that
    reader = ActLogReader(log, raise_on_invalid_id=error)
    data = parse_fights(reader)
    print_matrix(data)


def main():
    """Entrypoint to the cli app"""
    parser = create_parser()
    args: Namespace = parser.parse_args()
    handle_args(**vars(args))


if __name__ == '__main__':
    main()
