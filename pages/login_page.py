from locators.authorization_locators import LoginFormLocators
from pages.base_page import BasePage


class loginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def authorization(self, name_text, password_text):
        self.fill(value=name_text, locator=LoginFormLocators.NAME)
        self.fill(value=password_text, locator=LoginFormLocators.PASSWORD)
        self.click(LoginFormLocators.LOGIN_BUTTON)

    def reset_data(self):
        self.click(LoginFormLocators.RESET_BUTTON)

    def get_result_text(self):
        return self.text(LoginFormLocators.RESULT_TEXT)