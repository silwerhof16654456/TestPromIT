import pytest
from selenium.webdriver.common.keys import Keys
from pages.key_presses_page import KeyPressesPage

class TestKeyPresses:
    
    @pytest.mark.parametrize('key,expected', [
        (Keys.ESCAPE, 'ESCAPE'),
        (Keys.CONTROL, 'CONTROL'),
        (Keys.ENTER, 'ENTER'),
        (Keys.BACKSPACE, 'BACK_SPACE'),
        (Keys.TAB, 'TAB'),
        (Keys.SHIFT, 'SHIFT')
    ])
    def test_key_press(self, driver, key, expected):
        """Нажатие клавиш и проверка результата"""
        key_page = KeyPressesPage(driver)
        key_page.open()
        
        key_page.press_key(key)
        
        result = key_page.get_result_text()
        assert expected in result, f'Не отобразилось нажатие {expected}'