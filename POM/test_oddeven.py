import pytest
import sys

def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


class TestData:

    @pytest.mark.regression
    def test_even(self):
        assert even_odd(20) == "Even"

    def test_odd(self):
        assert even_odd(17) == "Odd"

    @pytest.mark.skip(reason="NOT VALID")
    def test_neutral(self):
        assert even_odd(1) == "not valid"

    @pytest.mark.skipif(sys.platform == "win32", reason="Runs on Windows")
    def test_fail(self):
        assert even_odd(0) == "Natural"