import pytest


@pytest.mark.smoke
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"

def test_SecondCreditCard():
    a = 4
    b = 6
    assert a+2 == b, "Addition does not match"