import os
import tempfile

import pytest
from selenium import webdriver

from pages.login_page import loginPage


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://berpress.github.io/selenium-login-demo/", help="URL")


@pytest.fixture(scope="session")
def login_page(request):
    url = request.config.getoption('--url')
    user_data_dir = os.path.join(tempfile.mkdtemp(), "chrome_profile")
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={user_data_dir}")
    options.add_argument("--no-sandbox")  # Важно для GitHub Actions!
    options.add_argument("--disable-dev-shm-usage")  # Для избежания ошибок памяти
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    login_page = loginPage(driver)
    yield login_page
    driver.quit()
