import pytest

@pytest.mark.usefixtures("setup")
class TestExamples:

    def test_fixtureDemo1(setup):
        print("I will execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(setup):
        print("I will execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(setup):
        print("I will execute steps in fixtureDemo3 method")

    def test_fixtureDemo4(setup):
        print("I will execute steps in fixtureDemo4 method")