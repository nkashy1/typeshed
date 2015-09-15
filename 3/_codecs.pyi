"""Stub file for the '_codecs' module."""
# This is an autogenerated file. It serves as a starting point
# for a more precise manual annotation of this module.
# Feel free to edit the source below, but remove this header when you do.

from typing import List, Tuple, Dict, GenericType

def _forget_codec(a: str) -> None: ...

def ascii_decode(a, *args, **kwargs) -> tuple: ...

def ascii_encode(a, *args, **kwargs) -> tuple: ...

def charmap_build(a: str) -> object: ...

def charmap_decode(a, *args, **kwargs) -> tuple: ...

def charmap_encode(a, *args, **kwargs) -> tuple: ...

def decode(a, *args, **kwargs) -> object: ...

def encode(a, *args, **kwargs) -> object: ...

def escape_decode(a, *args, **kwargs) -> tuple: ...

def escape_encode(a, *args, **kwargs) -> tuple:
    raise OverflowError()

def latin_1_decode(a, *args, **kwargs) -> tuple: ...

def latin_1_encode(a, *args, **kwargs) -> tuple: ...

def lookup(a: str) -> object: ...

def lookup_error(a: str) -> object: ...

def raw_unicode_escape_decode(a, *args, **kwargs) -> tuple: ...

def raw_unicode_escape_encode(a, *args, **kwargs) -> tuple: ...

def readbuffer_encode(a, *args, **kwargs) -> tuple: ...

def register(*args, **kwargs) -> None: ...

def register_error(a: str, b) -> None: ...

def unicode_escape_decode(a, *args, **kwargs) -> tuple: ...

def unicode_escape_encode(a, *args, **kwargs) -> tuple: ...

def unicode_internal_decode(a, *args, **kwargs) -> tuple: ...

def unicode_internal_encode(a, *args, **kwargs) -> tuple:
    raise DeprecationWarning()
    raise MemoryError()

def utf_16_be_decode(a, *args, **kwargs) -> tuple: ...

def utf_16_be_encode(a, *args, **kwargs) -> tuple: ...

def utf_16_decode(a, *args, **kwargs) -> tuple: ...

def utf_16_encode(a, *args, **kwargs) -> tuple: ...

def utf_16_ex_decode(a, *args, **kwargs) -> tuple: ...

def utf_16_le_decode(a, *args, **kwargs) -> tuple: ...

def utf_16_le_encode(a, *args, **kwargs) -> tuple: ...

def utf_32_be_decode(a, *args, **kwargs) -> tuple: ...

def utf_32_be_encode(a, *args, **kwargs) -> tuple: ...

def utf_32_decode(a, *args, **kwargs) -> tuple: ...

def utf_32_encode(a, *args, **kwargs) -> tuple: ...

def utf_32_ex_decode(a, *args, **kwargs) -> tuple: ...

def utf_32_le_decode(a, *args, **kwargs) -> tuple: ...

def utf_32_le_encode(a, *args, **kwargs) -> tuple: ...

def utf_7_decode(a, *args, **kwargs) -> tuple: ...

def utf_7_encode(a, *args, **kwargs) -> tuple: ...

def utf_8_decode(a, *args, **kwargs) -> tuple: ...

def utf_8_encode(a, *args, **kwargs) -> tuple: ...
