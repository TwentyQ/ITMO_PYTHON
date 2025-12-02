import io
import unittest

from decorator import logger
from function import get_currencies


class TestLoggerWithStringIO(unittest.TestCase):
    """Тесты для работы декоратора с StringIO"""

    def test_stringio_multiple_calls(self):
        """Тест нескольких вызовов с StringIO"""
        string_stream = io.StringIO()

        @logger(handle=string_stream)
        def counter_function(x):
            return x + 1

        # Несколько вызовов функции
        counter_function(1)
        counter_function(2)
        counter_function(3)

        logs = string_stream.getvalue()

        # Проверяем, что все вызовы записаны
        self.assertEqual(logs.count("Начать counter_function"), 3)
        self.assertEqual(logs.count("Успех counter_function"), 3)
        self.assertIn("Результат: 2", logs)
        self.assertIn("Результат: 3", logs)
        self.assertIn("Результат: 4", logs)

    def test_stringio_flush_behavior(self):
        """Тест поведения flush с StringIO"""
        string_stream = io.StringIO()

        @logger(handle=string_stream)
        def test_function():
            return "test"

        result = test_function()

        # Проверяем, что данные записаны в поток
        logs = string_stream.getvalue()
        self.assertIn("test_function", logs)
        self.assertEqual(result, "test")

    def test_stringio_large_output(self):
        """Тест с большим объемом вывода"""
        string_stream = io.StringIO()

        @logger(handle=string_stream)
        def large_output_function():
            return "x" * 1000  # Большая строка

        result = large_output_function()

        logs = string_stream.getvalue()
        self.assertIn("x" * 1000, logs)
        self.assertEqual(len(result), 1000)


class TestStreamWrite(unittest.TestCase):
    """Тесты для проверки записи в поток"""

    def setUp(self):
        """Подготовка тестового окружения"""
        self.stream = io.StringIO()

        @logger(handle=self.stream)
        def wrapped_function():
            return get_currencies(['USD'], url="https://invalid-url-test.com")

        self.wrapped_function = wrapped_function

    def test_logging_connection_error_in_stringio(self):
        """Тест логирования ошибки соединения в StringIO"""
        with self.assertRaises(ConnectionError):
            self.wrapped_function()

        logs = self.stream.getvalue()
        # Проверяем, что ошибка залогирована
        self.assertIn("ERROR", logs)
        self.assertIn("ConnectionError", logs)