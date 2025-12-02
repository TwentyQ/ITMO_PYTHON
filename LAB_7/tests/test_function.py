import unittest
from unittest.mock import patch, MagicMock
import requests

from function import get_currencies


class TestGetCurrencies(unittest.TestCase):
    """Тесты для функции get_currencies"""

    @patch('requests.get')
    def test_successful_response(self, test_get):
        """Тест успешного получения курсов валют"""
        # Создаем имитацию успешного ответа от API
        test_response = MagicMock()
        test_response.json.return_value = {
            "Valute": {
                "USD": {"Value": 93.25},
                "EUR": {"Value": 101.70},
                "GBP": {"Value": 115.45}
            }
        }
        # Задаем, что при вызове requests.get возвращается наш имитированный ответ
        test_get.return_value = test_response

        # Вызываем тестируемую функцию с списком валют
        result = get_currencies(['USD', 'EUR'])

        # Проверяем, что функция вернула правильный результат
        self.assertEqual(result, {'USD': 93.25, 'EUR': 101.70})
        # Проверяем, что функция действительно вызвала requests.get
        test_get.assert_called_once()

    @patch('requests.get')
    def test_connection_error(self, test_get):
        """Тест ошибки соединения с API"""
        # Имитируем ошибку соединения при вызове requests.get
        test_get.side_effect = requests.exceptions.ConnectionError("Connection failed")

        # Проверяем, что функция выбрасывает ConnectionError при ошибке сети
        with self.assertRaises(ConnectionError):
            get_currencies(['USD'])

    @patch('requests.get')
    def test_invalid_json(self, test_get):
        """Тест некорректного JSON в ответе"""
        test_response = MagicMock()
        # Имитируем ситуацию, когда response.json() вызывает ошибку
        test_response.json.side_effect = ValueError("Invalid JSON")
        test_get.return_value = test_response

        # Проверяем, что функция обрабатывает некорректный JSON как ValueError
        with self.assertRaises(ValueError):
            get_currencies(['USD'])

    @patch('requests.get')
    def test_missing_valute_key(self, test_get):
        """Тест отсутствия ключа 'Valute' в ответе"""
        test_response = MagicMock()
        # Создаем ответ API без необходимого ключа 'Valute'
        test_response.json.return_value = {"SomeOtherKey": {}}
        test_get.return_value = test_response

        # Проверяем, что функция обнаруживает отсутствие ключа 'Valute'
        with self.assertRaises(KeyError):
            get_currencies(['USD'])

    @patch('requests.get')
    def test_currency_not_found(self, test_get):
        """Тест запроса несуществующей валюты"""
        test_response = MagicMock()
        test_response.json.return_value = {
            "Valute": {
                "USD": {"Value": 93.25}  # В ответе есть только USD
            }
        }
        test_get.return_value = test_response

        # Пытаемся получить курс для валюты, которой нет в ответе
        with self.assertRaises(KeyError):
            get_currencies(['EUR'])  # Запрашиваем EUR, которой нет в данных

    @patch('requests.get')
    def test_invalid_currency_type(self, test_get):
        """Тест неверного типа курса валюты"""
        test_response = MagicMock()
        test_response.json.return_value = {
            "Valute": {
                "USD": {"Value": "invalid_string"}  # Курс валюты - строка вместо числа
            }
        }
        test_get.return_value = test_response

        # Проверяем, что функция обнаруживает неверный тип данных курса
        with self.assertRaises(TypeError):
            get_currencies(['USD'])