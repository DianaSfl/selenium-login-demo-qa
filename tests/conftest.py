import pytest
from selenium import webdriver

from pages.login_page import loginPage


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://berpress.github.io/selenium-login-demo/", help="URL")


@pytest.fixture(scope="session")
def login_page(request):
    url = request.config.getoption('--url')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome()
    driver.get(url)
    login_page = loginPage(driver)
    yield login_page
    driver.quit()
