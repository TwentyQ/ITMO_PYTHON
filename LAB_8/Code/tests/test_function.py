import unittest
from unittest.mock import patch, Mock
from utils.currencies_api import get_currencies


class TestCurrenciesAPI(unittest.TestCase):
    """
    Тестирование функции get_currencies из модуля currencies_api.
    """

    @patch('utils.currencies_api.requests.get')
    def test_get_currencies_success(self, mock_get):
        """
        Тест успешного получения курсов валют.
        """
        # Подготовка мок-ответа со всеми запрашиваемыми валютами
        mock_response = Mock()
        mock_response.json.return_value = {
            'Valute': {
                "USD": {"Value": 75.50, "Nominal": 1},
                "EUR": {"Value": 89.25, "Nominal": 1},
                "GBP": {"Value": 105.80, "Nominal": 1}
            }
        }
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        # Вызов функции
        result = get_currencies(["USD", "EUR", "GBP"])

        # Assert: Проверка результатов
        self.assertIn("USD", result)
        self.assertIn("EUR", result)
        self.assertIn("GBP", result)
        self.assertEqual(result["USD"], 75.50)
        self.assertEqual(result["EUR"], 89.25)
        self.assertEqual(result["GBP"], 105.80)

        # Проверка вызова API
        mock_get.assert_called_once()

    @patch('utils.currencies_api.requests.get')
    def test_get_currencies_network_error(self, mock_get):
        """
        Тест обработки сетевой ошибки.
        """
        mock_get.side_effect = Exception("Network error")

        with self.assertRaises(Exception):
            get_currencies(["USD", "EUR"])

    @patch('utils.currencies_api.requests.get')
    def test_get_currencies_invalid_json(self, mock_get):
        """
        Тест обработки невалидного JSON в ответе.
        """
        mock_response = Mock()
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_get.return_value = mock_response

        with self.assertRaises(ValueError):
            get_currencies(["USD", "EUR"])

    @patch('utils.currencies_api.requests.get')
    def test_get_currencies_missing_single_currency(self, mock_get):
        """
        Тест ситуации, когда одна из запрашиваемых валют отсутствует в ответе.
        Ожидается KeyError для отсутствующей валюты.
        """
        # Ответ содержит только USD, но запрашиваются USD и EUR
        mock_response = Mock()
        mock_response.json.return_value = {
            'Valute': {
                "USD": {"Value": 75.50, "Nominal": 1}
            }
        }
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        # Проверяем, что функция выбрасывает KeyError для EUR
        with self.assertRaises(KeyError) as context:
            get_currencies(["USD", "EUR"])

        # Дополнительная проверка текста ошибки
        self.assertIn("EUR", str(context.exception))

    @patch('utils.currencies_api.requests.get')
    def test_get_currencies_http_error(self, mock_get):
        """
        Тест обработки HTTP ошибки.
        """
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = Exception("HTTP 404")
        mock_get.return_value = mock_response

        with self.assertRaises(Exception):
            get_currencies(["USD"])

    @patch('utils.currencies_api.requests.get')
    def test_get_currencies_missing_valute_key(self, mock_get):
        """
        Тест обработки ответа без ключа 'Valute'.
        Ожидается KeyError.
        """
        mock_response = Mock()
        mock_response.json.return_value = {}  # Пустой ответ без Valute
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        with self.assertRaises(KeyError) as context:
            get_currencies(["USD", "EUR"])

        # Проверяем, что ошибка связана с отсутствием Valute
        self.assertIn("Valute", str(context.exception))

    @patch('utils.currencies_api.requests.get')
    def test_get_currencies_empty_valute_with_empty_request(self, mock_get):
        """
        Тест обработки пустого Valute при пустом запросе.
        Пустой список валют должен возвращать пустой словарь.
        """
        mock_response = Mock()
        mock_response.json.return_value = {
            'Valute': {}
        }
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        # Пустой запрос должен возвращать пустой словарь
        result = get_currencies([])
        self.assertEqual(result, {})

    @patch('utils.currencies_api.requests.get')
    def test_get_currencies_value_type_error(self, mock_get):
        """
        Тест обработки валюты с некорректным типом значения.
        Ожидается TypeError
        """
        mock_response = Mock()
        mock_response.json.return_value = {
            'Valute': {
                "USD": {"Value": None, "Nominal": 1},  # None вместо числа
                "EUR": {"Value": "не число", "Nominal": 1},  # Строка вместо числа
                "GBP": {"Value": 75.50, "Nominal": 1}  # Корректное значение
            }
        }
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        # USD с None должен вызвать TypeError
        with self.assertRaises(TypeError) as context:
            get_currencies(["USD", "EUR", "GBP"])

        # Проверяем, что ошибка связана с USD
        self.assertIn("USD", str(context.exception))

    @patch('utils.currencies_api.requests.get')
    def test_get_currencies_single_currency_success(self, mock_get):
        """
        Тест успешного получения одной валюты.
        """
        mock_response = Mock()
        mock_response.json.return_value = {
            'Valute': {
                "USD": {"Value": 75.50, "Nominal": 1}
            }
        }
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = get_currencies(["USD"])
        self.assertEqual(result, {"USD": 75.50})

    @patch('utils.currencies_api.requests.get')
    def test_get_currencies_duplicate_codes(self, mock_get):
        """
        Тест обработки дублирующихся кодов валют в запросе.
        """
        mock_response = Mock()
        mock_response.json.return_value = {
            'Valute': {
                "USD": {"Value": 75.50, "Nominal": 1},
                "EUR": {"Value": 89.25, "Nominal": 1}
            }
        }
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        # Запрос с дубликатами
        result = get_currencies(["USD", "EUR", "USD"])
        self.assertEqual(result, {"USD": 75.50, "EUR": 89.25})
        # Проверяем, что USD в результате только один раз
        self.assertEqual(len(result), 2)

    @patch('utils.currencies_api.requests.get')
    def test_get_currencies_case_sensitive(self, mock_get):
        """
        Тест чувствительности к регистру кодов валют.
        """
        mock_response = Mock()
        mock_response.json.return_value = {
            'Valute': {
                "USD": {"Value": 75.50, "Nominal": 1},
                "EUR": {"Value": 89.25, "Nominal": 1}
            }
        }
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        # Запрос в нижнем регистре должен вызвать ошибку
        with self.assertRaises(KeyError):
            get_currencies(["usd", "eur"])  # строчные буквы


if __name__ == '__main__':
    unittest.main()