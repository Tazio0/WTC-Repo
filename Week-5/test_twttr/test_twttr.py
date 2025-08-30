import pytest

from twttr import shorten

def test_short():
    assert shorten("hello, world") == "hll, wrld"
    assert shorten("HELLO, WORLD") == "HLL, WRLD"
    assert shorten("Go on 123!") == "G n 123!"