"""Byte-related utility functions"""

def hexstr_to_byte(string: str, pad: bool = True) -> int:
    """Converts a hexstring to a byte; items less than 4 characters 'wide' are padded"""
    if pad:
        return int(string.rjust(4, '0'), 16)
    return int(string, 16)
