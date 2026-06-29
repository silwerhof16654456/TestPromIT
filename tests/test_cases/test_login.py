import pytest
from pages.login_page import LoginPage

class TestLogin:
    
    def test_successful_login(self, driver):
        """Успешный вход с валидными данными"""
        login_page = LoginPage(driver)
        login_page.open()
        
        login_page.login('practice', 'SuperSecretPassword!')
        
        success_text = login_page.get_success_message()
        assert 'You logged into a secure area!' in success_text, 'Не удалось войти'
    
    def test_invalid_username(self, driver):
        """Вход с невалидным логином"""
        login_page = LoginPage(driver)
        login_page.open()
        
        login_page.login('wronguser', 'SuperSecretPassword!')
        
        error = login_page.get_error_message()
        assert 'Your password is invalid!' in error, 'Нет сообщения об ошибке'
    
    def test_invalid_password(self, driver):
        """Вход с валидным логином и невалидным паролем"""
        login_page = LoginPage(driver)
        login_page.open()
        
        login_page.login('practice', 'WrongPassword123')
        
        error = login_page.get_error_message()
        assert 'Your password is invalid!' in error, 'Нет сообщения об ошибке'
    
    def test_empty_fields(self, driver):
        """Вход с пустыми полями"""
        login_page = LoginPage(driver)
        login_page.open()
        
        login_page.login('', '')
        
        error = login_page.get_error_message()
        assert error != '', 'Нет сообщения об ошибке при пустых полях'