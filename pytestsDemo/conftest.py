import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")

@pytest.fixture()
def dataLoad():
    print("User profile is being created")
    return ["Rahul","Shetty","RahulShettyAcademy.com"]

@pytest.fixture(params=[("Chrome","Rahul","Shetty"),("Firefox","Shetty"),("IE","SS")])
def crossBrowser(request):
    return request.param