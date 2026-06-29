import pytest
from pages.inputs_page import InputsPage

class TestInputs:
    
    def test_fill_form_and_verify(self, driver):
        """Заполнение всех полей и проверка Output"""
        inputs_page = InputsPage(driver)
        inputs_page.open()
        
        test_data = {
            'number': '42',
            'text': 'Hello World!',
            'password': 'MySecret123',
            'date': '28.06.2026'
        }
        
        inputs_page.fill_form(
            test_data['number'],
            test_data['text'],
            test_data['password'],
            test_data['date']
        )
        
        inputs_page.click_display_button()
        
        output_number = inputs_page.get_output_number()
        output_text = inputs_page.get_output_text()
        output_password = inputs_page.get_output_password()
        output_date = inputs_page.get_output_date()
        
        assert test_data['number'] == output_number, f'Ожидалось {test_data["number"]}, получено {output_number}'
        assert test_data['text'] == output_text, f'Ожидалось {test_data["text"]}, получено {output_text}'
        assert test_data['password'] == output_password, f'Ожидалось {test_data["password"]}, получено {output_password}'
        
        date_parts = test_data['date'].split('.')
        expected_date = f'{date_parts[2]}-{date_parts[1]}-{date_parts[0]}'
        assert expected_date == output_date, f'Ожидалось {expected_date}, получено {output_date}'
    
    def test_clear_fields(self, driver):
        """Очистка полей после заполнения"""
        inputs_page = InputsPage(driver)
        inputs_page.open()
        
        inputs_page.fill_form('123', 'test', 'pass', '28.06.2026')
        inputs_page.click_display_button()
        inputs_page.click_clear_button()
        
        number_field = driver.find_element(*inputs_page.input_number)
        assert number_field.get_attribute('value') == '', 'Поле number не очистилось'
        
        text_field = driver.find_element(*inputs_page.input_text)
        assert text_field.get_attribute('value') == '', 'Поле text не очистилось'