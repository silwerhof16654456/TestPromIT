from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find(self, locator):
        """Найти элемент с ожиданием"""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except:
            return None
    
    def click(self, locator):
        """Кликнуть по элементу"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except:
            print('Элемент не найден или не кликабелен, пропускаем клик')
    
    def input_text(self, locator, text):
        """Ввести текст в поле"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.clear()
            element.send_keys(text)
        except:
            print('Не удалось ввести текст')
    
    def get_text(self, locator):
        """Получить текст элемента"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text
        except:
            return ''
    
    def wait_for_visible(self, locator):
        """Дождаться видимости элемента"""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except:
            return None