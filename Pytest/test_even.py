import pytest

def even_odd(n):
    if n % 2 ==0:
        return "Even"
    else:
        return "Odd"

def test_even_odd():
    assert even_odd(20) == 'Even'
    print("Even")

def test_odd():
    assert even_odd(13) == "Odd"
    print("Odd")

