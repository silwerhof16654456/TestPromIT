from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class KeyPressesPage(BasePage):
    target = (By.ID, 'target')
    result = (By.ID, 'result')
    
    def open(self):
        """Открыть страницу Key Presses"""
        self.driver.get('https://practice.expandtesting.com/key-presses')
        self.wait.until(EC.presence_of_element_located(self.target))
    
    def press_key(self, key):
        """Нажать клавишу в поле"""
        element = self.wait.until(EC.element_to_be_clickable(self.target))
        element.click()
        element.send_keys(key)
        self.wait.until(EC.presence_of_element_located(self.result))
    
    def get_result_text(self):
        """Получить текст результата"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.result))
            return element.text
        except:
            return ''