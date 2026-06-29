from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class ForgotPasswordPage(BasePage):
    email_input = (By.ID, 'email')
    submit_button = (By.XPATH, '//button[@type="submit"]')
    error_message = (By.CSS_SELECTOR, '.alert-danger')
    success_message = (By.CSS_SELECTOR, '.alert-info')
    invalid_feedback = (By.CSS_SELECTOR, '.invalid-feedback')
    
    def open(self):
        """Открыть страницу восстановления пароля"""
        self.driver.get('https://practice.expandtesting.com/forgot-password')
        self.wait.until(EC.presence_of_element_located(self.email_input))
    
    def enter_email(self, email):
        """Ввести email"""
        element = self.wait.until(EC.element_to_be_clickable(self.email_input))
        element.clear()
        element.send_keys(email)
    
    def submit(self):
        """Нажать кнопку отправки"""
        button = self.wait.until(EC.element_to_be_clickable(self.submit_button))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        button.click()
    
    def get_error_text(self):
        """Получить текст ошибки"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.error_message))
            return element.text
        except:
            return ''
    
    def get_success_text(self):
        """Получить текст успешного сообщения"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.success_message))
            return element.text
        except:
            return ''
    
    def get_invalid_feedback_text(self):
        """Получить текст валидации HTML5"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.invalid_feedback))
            return element.text
        except:
            return ''