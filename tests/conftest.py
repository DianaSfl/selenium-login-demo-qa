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
    options = webdriver.ChromeOptions()

    if os.getenv('GITHUB_ACTIONS') == 'true':
        # Настройки для GitHub Actions
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
    else:
        # Настройки для локального запуска
        user_data_dir = os.path.join(tempfile.mkdtemp(), "chrome_profile")
        options.add_argument(f"--user-data-dir={user_data_dir}")
        options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)  # Добавляем неявное ожидание
    driver.get(url)

    try:
        login_page = loginPage(driver)
        yield login_page
    finally:
        driver.quit()
