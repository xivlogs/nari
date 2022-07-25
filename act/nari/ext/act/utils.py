"""Helpful utiliites"""
from enum import Enum
from datetime import datetime
from hashlib import md5, sha256

from nari.types import Timestamp

from nari.ext.act.exceptions import InvalidActChecksumAlgorithm


DEFAULT_DATE_FORMAT: str = '%Y-%m-%dT%H:%M:%S.%f%z'


# pylint: disable=invalid-name
class ActLogChecksumType(Enum):
    """List of hashsum algorithms used by different ACT versions"""
    MD5 = "md5"
    SHA256 = "sha256"
# pylint: enable=invalid-name


def date_from_act_timestamp(datestr: str) -> Timestamp:
    """Parse timestamp from ACT log into a Timestamp
    Look, this is dirty. This is wrong. Please someone find a better way to do this.
    """
    return int(datetime.strptime(f'{datestr[:26]}{datestr[-6:]}', DEFAULT_DATE_FORMAT).timestamp() * 1000)


def validate_checksum(line: str, index: int, algo: ActLogChecksumType = ActLogChecksumType.SHA256) -> bool:
    """Validates an ACT log line
    Given some line 1|foo|bar|baz|a823425f532c540667195f641dd3649b, and an index of 1, then the md5sum of
    1|foo|bar|baz|1 (where 1 is the index) should be a823425f532c540667195f641dd3649b (which is the checksum value)
    """
    parts = line.split('|')
    check_hash = parts[-1]
    to_hash = f'{"|".join(parts[:-1])}|{index}'.encode('utf-8')

    match algo:
        case ActLogChecksumType.MD5:
            return md5(to_hash).hexdigest() == check_hash
        case ActLogChecksumType.SHA256:
            return sha256(to_hash).hexdigest()[:16] == check_hash
        case _:
            raise InvalidActChecksumAlgorithm(f'Unexpected checksum algorithm: {algo}. Expected one of MD5 and SHA256.')
