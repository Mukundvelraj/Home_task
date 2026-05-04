import pytest

def even_num(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"

def test_even_odd():
    even = []
    odd = []
    for i in range(1,10+1):
        if i % 2 == 0:
            assert even_num(i) == "Even"
            even.append(i)
        else:
            assert even_num(i) == "Odd"
            odd.append(i)
    print(f"Even : {even}")
    print(f"Odd : {odd}")