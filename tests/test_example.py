import pytest


@pytest.mark.slow
def test_fail():
    assert False
