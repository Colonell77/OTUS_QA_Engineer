import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Какой браузер использовать?")
    parser.addoption("--url", action="store", default="http://test.r90244di.beget.tech/", help="This is request url")


@pytest.fixture
def get_driver(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    if browser == 'gecko':
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    elif browser == 'edge':
        driver = webdriver.Edge('msedgedriver.exe')
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

    yield driver, url
    driver.close()
    driver.quit()


