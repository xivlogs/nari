#!/usr/bin/env python3.8
"""Entrypoint into the base nari cli client"""

from argparse import ArgumentParser, Namespace
from logging import basicConfig, getLogger, Logger, CRITICAL, INFO
from typing import TypeVar

from nari.ext.act import ActLogReader
from nari.io.reader import Reader
from nari.types.event.instance import InstanceComplete, InstanceFade, InstanceInit


DEFAULT_LOG_FORMAT: str = '[%(levelname)s] %(message)s'
logger: Logger = getLogger('nari')

T = TypeVar('T') # pylint: disable=invalid-name
Matrix = list[list[T]]


def print_matrix(matrix: Matrix[str]):
    """Hacky function to print out an 'aligned' set of data"""
    col_width = max(len(word) for row in matrix for word in row) + 2
    for row in matrix:
        print(''.join(word.ljust(col_width) for word in row))


def parse_fights(reader: Reader) -> Matrix[str]:
    """Takes in a reader object and parses the fight details out of it"""
    column_headers: list[str] = ['date', 'instance id', 'encounters']
    matrix = [column_headers]
    fight_log: list[dict] = []
    current_fight: dict = {}

    for event in filter(lambda e: isinstance(e, (InstanceInit, InstanceFade, InstanceComplete)), reader):
        if isinstance(event, InstanceInit):
            if current_fight:
                fight_log.append(current_fight)
            current_fight = {
                'date': event.timestamp,
                'name': str(event.instance_id),
            }
        elif isinstance(event, (InstanceFade, InstanceComplete)):
            current_fight['fights'] = current_fight.get('fights', 0) + 1

    # wrap up any lingering fights
    if current_fight:
        fight_log.append(current_fight)

    for fight in fight_log:
        num_fights = fight.get('fights', 0)
        amtstr = 'fight' if num_fights == 1 else 'fights'
        matrix.append([
            f'[{fight["date"]}]',
            fight['name'],
            f'{num_fights} {amtstr}'
        ])

    return matrix


def create_parser() -> ArgumentParser:
    """Convenience function to create the argument parser"""
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
