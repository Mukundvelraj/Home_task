import pytest
import sys

@pytest.mark.skip(reason="Not ready")
def test_skip():
    assert True

@pytest.mark.skipif(sys.platform == "win32", reason="Windows issue")
def test_skipif():
    assert True

@pytest.mark.xfail(reason="Bug #123")
def test_xfail():
    assert False

@pytest.mark.xfail(strict=True, reason="Critical bug")
def test_xfail_strict():
    assert True