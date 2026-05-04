import pytest


@pytest.mark.slow
def test_run1():
    assert True
    print("Slow")

@pytest.mark.regression
def test_run2():
    assert True
    print("Regression")

@pytest.mark.smoke
def test_run3():
    assert True
    print("Smoke")

@pytest.mark.xfail
def test_run4():
    assert True
    print(f"Xfail")