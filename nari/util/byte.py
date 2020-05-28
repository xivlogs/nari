from typing import List


def hexstr_to_byte(string: str, pad: bool = True) -> int:
    if pad:
        return int(string.rjust(4, '0'), 16)
    return int(string, 16)


def reverse_bytes(bytes: List[int]) -> List[int]:
    return list(reversed(bytes))