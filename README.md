# Тестовое для PromIT

Сайт-песочница: https://practice.expandtesting.com

## Содержание

- [Технологии](#технологии)
- [Структура проекта](#структура-проекта)
- [Установка и запуск](#установка-и-запуск)
- [Результаты тестов](#результаты-тестов)
- [Известные проблемы](#известные-проблемы)

## Технологии

- Python 3.14
- Selenium WebDriver
- pytest
- Page Object Model

## Структура проекта
conftest.py # Настройка драйвера
requirements.txt # Зависимости
README.md # Описание проекта

pages/
- base_page.py # Базовый класс для всех страниц
- login_page.py # Страница логина
- inputs_page.py # Страница Inputs
- forgot_password_page.py # Страница восстановления пароля
- checkboxes_page.py # Страница Checkboxes
- key_presses_page.py # Страница Key Presses
- autocomplete_page.py # Страница Autocomplete

tests/
- test_cases/
- test_login.py
- test_inputs.py
- test_forgot_password.py
- test_checkboxes.py
- test_key_presses.py
- test_autocomplete.py

## Установка и запуск

1 Клонировать репозиторий
```bash
git clone https://github.com/silwerhof16654456/TestPromIT.git
cd TestPromIT
```
2 Создать и активировать виртуальное окружение
```bash
python -m venv .venv
.venv\Scripts\activate
```
3 Установить зависимости
```bash
pip install -r requirements.txt
```
4 Запустить все тесты
```bash
pytest -v
```
5 Запустить конкретный тест
```bash
pytest tests/test_cases/test_login.py -v
```
## Результаты тестов

| Раздел | Тестов | Результат |
|-----------|--------|-----------|
| Autocomplete | 1 | PASSED |
| Checkboxes | 4 | PASSED |
| Forgot Password | 7 | PASSED |
| Inputs | 2 | PASSED |
| Key Presses | 6 | 5 PASSED, 1 FAILED |
| Login | 4 | PASSED |
| **ИТОГО** | **24** | **23 PASSED, 1 FAILED** |

## Известные проблемы
**Key Presses - ENTER**  тест падает, так как нажатие Enter на странице вызывает перезагрузку (отправку формы), а не отображение результата. Остальные клавиши работают корректно.
