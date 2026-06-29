import pytest
from pages.forgot_password_page import ForgotPasswordPage

class TestForgotPassword:
    
    @pytest.mark.parametrize('email,expected_error', [
        ('', 'Please enter a valid email address.'),
        ('notanemail', 'Please enter a valid email address.'),
        ('test@', 'Please enter a valid email address.'),
        ('test@domain', 'Your email is invalid!'),
        ('user@site.com', ''),
        ('a@b.c', ''),
        ('very.long.email.address@very.long.domain.name.com', '')
    ])
    def test_email_validation(self, driver, email, expected_error):
        """Проверка валидации email"""
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open()
        
        forgot_page.enter_email(email)
        forgot_page.submit()
        
        if expected_error:
            if 'Please enter a valid email address.' in expected_error:
                error = forgot_page.get_invalid_feedback_text()
            else:
                error = forgot_page.get_error_text()
            assert expected_error in error, f'Ожидалась ошибка: {expected_error}'
        else:
            success = forgot_page.get_success_text()
            assert 'An e-mail has been sent to you' in success, 'Не пришло письмо'