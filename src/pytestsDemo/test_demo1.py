# Any PyTest file should start with "test_" or end with "_test"
# PyTest method name should start with "test"
# Any Code should be wrapped in method only
# Method name should be having sense
import pytest


# "-k" stands for method names execution
# "-v" stands for more info metadata
# "-s" stands for logs in output
# Running specific py file to be executed
# "-m" stands for Mark / Tags - you can mark "@pytest.mark.smoke"
# you can skip the test by providing "@pytest.mark.skip"
# Fixtures are used for setup and tear down methods for test cases - conftest file to generalize
# Fixtures and make it available to all test cases
# Data Driven and parameterization can be done in return statement in Tuple format
# When you define scope to class only , it will run once before class is initiated

@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    print("Hello")

@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")

def test_CrossBrowser(crossBrowser):
    print(crossBrowser[1])