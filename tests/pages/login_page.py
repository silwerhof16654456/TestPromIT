from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage(BasePage):
    username_input = (By.ID, 'username')
    password_input = (By.ID, 'password')
    login_button = (By.XPATH, '//button[@type="submit"]')
    success_message = (By.CSS_SELECTOR, '.alert-success')
    error_message = (By.CSS_SELECTOR, '.alert-danger')
    
    def open(self):
        """Открыть страницу логина"""
        self.driver.get('https://practice.expandtesting.com/login')
        self.wait.until(EC.presence_of_element_located(self.username_input))
    
    def login(self, username, password):
        """Выполнить вход"""
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        
        button = self.wait.until(EC.presence_of_element_located(self.login_button))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        time.sleep(0.5)
        button.click()
    
    def get_success_message(self):
        """Получить сообщение об успехе"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.success_message))
            return element.text
        except:
            return ''
    
    def get_error_message(self):
        """Получить сообщение об ошибке"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.error_message))
            return element.text
        except:
            return ''