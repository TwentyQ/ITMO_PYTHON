import unittest
from unittest.mock import MagicMock
from controllers.currencycontroller import CurrencyController


class TestCurrencyController(unittest.TestCase):
    """Тесты для контроллера валют."""

    def test_list_currencies(self):
        """Тест получения списка валют."""
        # Создаем мок-объект базы данных
        mock_db = MagicMock()
        mock_db._read.return_value = [{"id": 1, "char_code": "USD", "value": 90}]

        # Создаём контроллер с мок-базой
        controller = CurrencyController(mock_db)

        # Вызываем тестируемый метод
        result = controller.list_currencies()

        # Проверяем результат
        self.assertEqual(result[0]['char_code'], "USD")
        self.assertEqual(result[0]['id'], 1)
        mock_db._read.assert_called_once()

    def test_update_currency(self):
        """Тест обновления курса валюты."""
        mock_db = MagicMock()
        controller = CurrencyController(mock_db)

        # Обновляем курс USD
        controller.update_currency("USD", 95.5)

        # Проверяем, что метод _update был вызван с правильными аргументами
        mock_db._update.assert_called_once_with({"USD": 95.5})

    def test_delete_currency(self):
        """Тест удаления валюты по ID."""
        mock_db = MagicMock()
        controller = CurrencyController(mock_db)

        # Удаляем валюту с ID 3
        controller.delete_currency(3)

        # Проверяем вызов метода удаления
        mock_db._delete.assert_called_once_with(3)

    def test_update_currency_with_different_codes(self):
        """Тест обновления курсов разных валют."""
        mock_db = MagicMock()
        controller = CurrencyController(mock_db)

        # Обновляем несколько валют
        controller.update_currency("USD", 92.0)
        controller.update_currency("EUR", 88.5)
        controller.update_currency("CNY", 12.8)

        # Проверяем, что метод вызывался 3 раза с правильными параметрами
        self.assertEqual(mock_db._update.call_count, 3)

        # Получаем все вызовы
        calls = mock_db._update.call_args_list

        # Проверяем параметры каждого вызова
        self.assertEqual(calls[0][0][0], {"USD": 92.0})
        self.assertEqual(calls[1][0][0], {"EUR": 88.5})
        self.assertEqual(calls[2][0][0], {"CNY": 12.8})

    def test_get_users(self):
        """Тест получения списка всех пользователей."""
        mock_db = MagicMock()
        # Настраиваем мок для возврата тестовых данных
        test_users = [
            {"id": 1, "name": "Кристина Лыскова"},
            {"id": 2, "name": "Елизавета Сунгуртян"},
            {"id": 3, "name": "Марина Максименко"}
        ]
        mock_db._read.return_value = test_users
        controller = CurrencyController(mock_db)

        # Получаем список пользователей
        result = controller.get_users()

        # Проверяем результат
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0]['name'], "Кристина Лыскова")
        self.assertEqual(result[1]['id'], 2)
        # Проверяем, что метод вызван с флагом get_users=True
        mock_db._read.assert_called_once_with(get_users=True)

    def test_get_user_currencies(self):
        """Тест получения валют пользователя."""
        mock_db = MagicMock()
        # Настраиваем мок для возврата тестовых данных
        test_data = [
            {"id": 1, "char_code": "USD", "name": "Доллар США", "value": 90.0, "num_code": "840", "nominal": 1},
            {"id": 2, "char_code": "EUR", "name": "Евро", "value": 95.5, "num_code": "978", "nominal": 1}
        ]
        mock_db._read.return_value = test_data
        controller = CurrencyController(mock_db)

        # Получаем валюты пользователя с ID 5
        result = controller.get_user_currencies(5)

        # Проверяем результат
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['char_code'], "USD")
        self.assertEqual(result[1]['name'], "Евро")
        # Проверяем, что метод вызван с правильным user_id
        mock_db._read.assert_called_once_with(user_id=5)
