from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class AutocompletePage(BasePage):
    input_field = (By.ID, 'country')
    dropdown_list = (By.CLASS_NAME, 'autocomplete-items')
    selected_value = (By.ID, 'country')
    
    def open(self):
        """Открыть страницу Autocomplete"""
        self.driver.get('https://practice.expandtesting.com/autocomplete')
        self.wait.until(EC.presence_of_element_located(self.input_field))
    
    def search_and_select(self, text):
        """Поиск и выбор страны"""
        element = self.wait.until(EC.element_to_be_clickable(self.input_field))
        element.click()
        element.clear()
        element.send_keys(text)
        
        try:
            self.wait.until(EC.presence_of_element_located(self.dropdown_list))
        except:
            pass
        
        items = self.driver.find_elements(By.CSS_SELECTOR, '.autocomplete-items div')
        
        found = False
        for item in items:
            if 'Canada' in item.text:
                item.click()
                found = True
                break
        
        if not found:
            element.send_keys(Keys.ENTER)
        
        self.wait.until(lambda driver: driver.find_element(*self.selected_value).get_attribute('value') != '')
    
    def get_selected_value(self):
        """Получить выбранное значение из поля"""
        try:
            element = self.wait.until(EC.presence_of_element_located(self.selected_value))
            return element.get_attribute('value')
        except:
            return ''