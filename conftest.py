import pytest
from config.driver_factory import get_driver

@pytest.fixture(autouse=True)
def setup(request):
    driver = get_driver()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()



# This is alternative options since storing credentials as raw text is not too good practice
def pytest_addoption(parser):
    parser.addoption("--username", action="store", help="Username to login with")
    parser.addoption("--password", action="store", help="Password to user to login with")


@pytest.fixture
def username(request):
    return request.config.getoption("--username")

@pytest.fixture
def password(request):
    return request.config.getoption("--password")

