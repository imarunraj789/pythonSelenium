import pytest


@pytest.fixture
def sample_data():
    print("\nSetup: Creating test data") #Runs before the test
    data = {"name":"Alice","age":30}
    yield data
    print("Cleaning up test data")

def test_example(sample_data):
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30
    print("Test executed successfully")