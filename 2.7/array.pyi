"""Stub file for the 'array' module."""
# This is an autogenerated file. It serves as a starting point
# for a more precise manual annotation of this module.
# Feel free to edit the source below, but remove this header when you do.

from typing import List, Tuple, Dict, GenericType

class array(object):
    def __copy__() -> object: ...
    def __deepcopy__(*args, **kwargs) -> object: ...
    def __reduce__() -> tuple:
        raise AttributeError()
    def __sizeof__() -> long: ...
    def append(*args, **kwargs) -> None: ...
    def buffer_info() -> tuple: ...
    def byteswap() -> None:
        raise RuntimeError()
    def count(*args, **kwargs) -> int: ...
    def extend(*args, **kwargs) -> None: ...
    def fromfile(a, b: int) -> None:
        raise EOFError()
        raise IOError()
        raise MemoryError()
        raise TypeError()
    def fromlist(*args, **kwargs) -> None:
        raise MemoryError()
        raise TypeError()
    def fromstring(a) -> None:
        raise MemoryError()
        raise ValueError()
    def fromunicode(a: str) -> None:
        raise MemoryError()
        raise ValueError()
    def index(*args, **kwargs) -> int:
        raise ValueError()
    def insert(a: int, b) -> None: ...
    def pop(*args, **kwargs) -> object:
        raise IndexError()
    def read(*args, **kwargs) -> None:
        raise DeprecationWarning()
    def remove(*args, **kwargs) -> None:
        raise ValueError()
    def reverse() -> None: ...
    def tofile(*args, **kwargs) -> None:
        raise IOError()
        raise TypeError()
    def tolist() -> list: ...
    def tostring() -> str:
        raise MemoryError()
    def tounicode() -> unicode:
        raise ValueError()
    def write(*args, **kwargs) -> None:
        raise DeprecationWarning()

class arrayiterator(object):
    pass
