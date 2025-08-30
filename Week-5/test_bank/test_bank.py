import pytest
from bank import value

def test_value_0():
    assert value("hello world") == 0
    assert value("Hello World") == 0

def test_value_20():
    assert value("hi world") == 20
    assert value("Hi World") == 20

def test_value_100():
    assert value("Good day") == 100
    assert value("good day") == 100
