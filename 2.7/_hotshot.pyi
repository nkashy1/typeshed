"""Stub file for the '_hotshot' module."""
# This is an autogenerated file. It serves as a starting point
# for a more precise manual annotation of this module.
# Feel free to edit the source below, but remove this header when you do.

from typing import List, Tuple, Dict, GenericType

def coverage(a: str) -> object: ...

def logreader(a: str) -> LogReaderType:
    raise IOError()
    raise RuntimeError()

def profiler(a: str, *args, **kwargs) -> object:
    raise IOError()

def resolution() -> tuple: ...


class LogReaderType(object):
    def close() -> None: ...
    def fileno() -> int:
        raise ValueError()

class ProfilerType(object):
    def addinfo(a: str, b: str) -> None: ...
    def close() -> None: ...
    def fileno() -> int:
        raise ValueError()
    def runcall(*args, **kwargs) -> object: ...
    def runcode(a, b, *args, **kwargs) -> object:
        raise TypeError()
    def start() -> None: ...
    def stop() -> None: ...
