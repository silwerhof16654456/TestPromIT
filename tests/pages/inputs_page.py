from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class InputsPage(BasePage):
    input_number = (By.CSS_SELECTOR, 'input[type="number"]')
    input_text = (By.CSS_SELECTOR, 'input[type="text"]')
    input_password = (By.CSS_SELECTOR, 'input[type="password"]')
    input_date = (By.CSS_SELECTOR, 'input[type="date"]')
    
    display_button = (By.ID, 'btn-display-inputs')
    clear_button = (By.ID, 'btn-clear-inputs')
    
    output_number = (By.ID, 'output-number')
    output_text = (By.ID, 'output-text')
    output_password = (By.ID, 'output-password')
    output_date = (By.ID, 'output-date')
    
    def open(self):
        """Открыть страницу Inputs"""
        self.driver.get('https://practice.expandtesting.com/inputs')
        self.wait.until(EC.presence_of_element_located(self.input_text))
    
    def fill_form(self, number, text, password, date):
        """Заполнить все поля формы"""
        self.driver.find_element(*self.input_number).send_keys(number)
        self.driver.find_element(*self.input_text).send_keys(text)
        self.driver.find_element(*self.input_password).send_keys(password)
        
        date_field = self.wait.until(EC.element_to_be_clickable(self.input_date))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", date_field)
        date_field.click()
        date_field.clear()
        date_field.send_keys(date)
    
    def click_display_button(self):
        """Нажать кнопку Display Inputs"""
        button = self.wait.until(EC.element_to_be_clickable(self.display_button))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        button.click()
        self.wait.until(EC.visibility_of_element_located(self.output_number))
    
    def click_clear_button(self):
        """Нажать кнопку Clear Inputs"""
        button = self.wait.until(EC.element_to_be_clickable(self.clear_button))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        button.click()
        self.wait.until(EC.visibility_of_element_located(self.input_text))
    
    def get_output_number(self):
        """Получить значение Number из Output"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.output_number))
            return element.text
        except:
            return ''
    
    def get_output_text(self):
        """Получить значение Text из Output"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.output_text))
            return element.text
        except:
            return ''
    
    def get_output_password(self):
        """Получить значение Password из Output"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.output_password))
            return element.text
        except:
            return ''
    
    def get_output_date(self):
        """Получить значение Date из Output"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.output_date))
            return element.text
        except:
            return ''