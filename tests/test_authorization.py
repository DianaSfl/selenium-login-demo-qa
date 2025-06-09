import time

class TestLoginForm:
    def test_login_valid_data(self, login_page):
        login_page.authorization(name_text='admin', password_text='password')
        time.sleep(1)
        result_text = login_page.get_result_text()
        assert "Успешно! Вход выполнен." in result_text, "Вход не выполнен"
        login_page.reset_data()

    def test_login_invalid_name(self, login_page):
        login_page.authorization(name_text='user', password_text='password')
        time.sleep(1)
        result_text = login_page.get_result_text()
        assert "Ошибка: Неверный логин или пароль." in result_text, "Вход с невалидными данными"
        login_page.reset_data()

    def test_login_invalid_password(self, login_page):
        login_page.authorization(name_text='admin', password_text='invalid password')
        time.sleep(1)
        result_text = login_page.get_result_text()
        assert "Ошибка: Неверный логин или пароль." in result_text, "Вход с невалидными данными"
        login_page.reset_data()

