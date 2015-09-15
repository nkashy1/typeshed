"""Stub file for the 'time' module."""
# This is an autogenerated file. It serves as a starting point
# for a more precise manual annotation of this module.
# Feel free to edit the source below, but remove this header when you do.

from typing import List, Tuple, Dict, GenericType

def asctime(*args, **kwargs) -> unicode: ...

def clock() -> float: ...

def clock_getres(a: int) -> float:
    raise IOError()

def clock_gettime(a: int) -> float:
    raise IOError()

def clock_settime(a: int, b) -> None:
    raise IOError()

def ctime(*args, **kwargs) -> unicode: ...

def get_clock_info(a: str) -> object:
    raise ValueError()

def gmtime(*args, **kwargs) -> tuple:
    raise OSError()

def localtime(*args, **kwargs) -> tuple: ...

def mktime(*args, **kwargs) -> float:
    raise OverflowError()

def monotonic() -> float: ...

def perf_counter() -> float: ...

def process_time() -> float: ...

def sleep(a: float) -> None:
    raise ValueError()

def strftime(a: str, *args, **kwargs) -> unicode:
    raise MemoryError()

def strptime(*args, **kwargs) -> object: ...

def time() -> float: ...

def tzset() -> None: ...
