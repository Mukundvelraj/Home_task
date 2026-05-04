import pytest

def square(value):
    val = value ** 2
    return val

@pytest.mark.parametrize("num,expected",[(2,4),(5,25),(6,36)])
def test_double(num,expected):
    assert square(num) == expected
    print(f"The {num} & its square : {square(num)}")

