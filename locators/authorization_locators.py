from selenium.webdriver.common.by import By
class LoginFormLocators:
    NAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-btn')
    RESET_BUTTON = (By.ID, 'reset-btn')

    RESULT_TEXT = (By.ID, 'result')