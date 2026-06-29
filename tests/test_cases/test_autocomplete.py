import pytest
from pages.autocomplete_page import AutocompletePage

class TestAutocomplete:
    
    def test_search_canada(self, driver):
        """Поиск и выбор страны Canada"""
        autocomplete_page = AutocompletePage(driver)
        autocomplete_page.open()
        
        autocomplete_page.search_and_select('Can')
        
        selected = autocomplete_page.get_selected_value()
        assert 'Canada' in selected, f'Не удалось выбрать Canada, выбрано: {selected}'