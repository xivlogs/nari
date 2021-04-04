"""Byte-related utility functions"""


def hexstr_to_int(string: str, pad: bool = True) -> int:
    """Converts a hexstring to a byte; items less than 4 characters 'wide' are padded"""
    if pad:
        return int(string.zfill(4), 16)
    return int(string, 16)


def hexstr_to_bytes(param: str) -> bytes:
    """Helper function to convert strings into bytes. Also changes the byte order."""

    param_expanded = param.zfill(8)
    bytes_arr = bytearray.fromhex(param_expanded)
    bytes_arr.reverse()  # switch the endianness

    return bytes(bytes_arr)
