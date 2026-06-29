from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CheckboxesPage(BasePage):
    checkbox_1 = (By.ID, 'checkbox1')
    checkbox_2 = (By.ID, 'checkbox2')
    
    def open(self):
        """Открыть страницу с чекбоксами"""
        self.driver.get('https://practice.expandtesting.com/checkboxes')
        self.wait.until(EC.presence_of_element_located(self.checkbox_1))
    
    def select_checkbox(self, index):
        """Выбрать чекбокс по индексу"""
        if index == 1:
            locator = self.checkbox_1
        else:
            locator = self.checkbox_2
        
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            if not element.is_selected():
                element.click()
        except:
            print(f'Не удалось выбрать чекбокс {index}')
    
    def deselect_checkbox(self, index):
        """Снять выбор с чекбокса"""
        if index == 1:
            locator = self.checkbox_1
        else:
            locator = self.checkbox_2
        
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            if element.is_selected():
                element.click()
        except:
            print(f'Не удалось снять чекбокс {index}')
    
    def is_checkbox_selected(self, index):
        """Проверить состояние чекбокса"""
        if index == 1:
            locator = self.checkbox_1
        else:
            locator = self.checkbox_2
        
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element.is_selected()
        except:
            return False
    
    def refresh_page(self):
        """Обновить страницу"""
        self.driver.refresh()
        self.wait.until(EC.presence_of_element_located(self.checkbox_1))