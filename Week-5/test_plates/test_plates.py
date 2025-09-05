import pytest

from plates import is_valid

def test_length():
    assert is_valid("CS") == True
    assert is_valid("C") == False
    assert is_valid("CSP5012") == False

def test_alphabet():
    assert is_valid("CS50") == True
    assert is_valid("C1") == False
    assert is_valid("1PF") == False

def test_number():
    assert is_valid("CS04") == False
    assert is_valid("123") == False
    assert is_valid("CS123P") == False

def test_alphanum():
    assert is_valid("A B") == False
    assert is_valid("AB?") == False
    assert is_valid("AB-34") == False
