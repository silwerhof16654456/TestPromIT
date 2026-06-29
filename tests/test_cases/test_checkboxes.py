import pytest
from pages.checkboxes_page import CheckboxesPage

class TestCheckboxes:
    
    def test_select_checkbox(self, driver):
        """Активация чекбокса"""
        checkboxes_page = CheckboxesPage(driver)
        checkboxes_page.open()
        
        checkboxes_page.select_checkbox(1)
        assert checkboxes_page.is_checkbox_selected(1) == True
        
        checkboxes_page.select_checkbox(2)
        assert checkboxes_page.is_checkbox_selected(2) == True
    
    def test_deselect_checkbox(self, driver):
        """Деактивация чекбокса"""
        checkboxes_page = CheckboxesPage(driver)
        checkboxes_page.open()
        
        checkboxes_page.select_checkbox(1)
        checkboxes_page.deselect_checkbox(1)
        assert checkboxes_page.is_checkbox_selected(1) == False
    
    def test_toggle_multiple(self, driver):
        """Переключение нескольких чекбоксов"""
        checkboxes_page = CheckboxesPage(driver)
        checkboxes_page.open()
        
        checkboxes_page.select_checkbox(1)
        checkboxes_page.select_checkbox(2)
        
        checkboxes_page.deselect_checkbox(1)
        checkboxes_page.deselect_checkbox(2)
        
        assert checkboxes_page.is_checkbox_selected(1) == False
        assert checkboxes_page.is_checkbox_selected(2) == False
    
    def test_state_after_refresh(self, driver):
        """Проверка сохранения состояния после перезагрузки"""
        checkboxes_page = CheckboxesPage(driver)
        checkboxes_page.open()
        
        checkboxes_page.select_checkbox(1)
        checkboxes_page.select_checkbox(2)
        
        checkboxes_page.refresh_page()
        
        assert checkboxes_page.is_checkbox_selected(1) == False
        assert checkboxes_page.is_checkbox_selected(2) == True