import unittest
import logging
import requests.exceptions

# Импортируем декоратор из основного кода
from decorator import logger  # замените your_main_file на имя вашего файла с декоратором


class TestLoggerDecoratorSimple(unittest.TestCase):
    """Простые тесты для декоратора logger"""

    def test_successful_execution_default_stdout(self):
        """Тест успешного выполнения с stdout по умолчанию"""

        # Используем декоратор logger из основного кода
        @logger
        def add_numbers(a, b):
            return a + b

        result = add_numbers(10, 5)
        self.assertEqual(result, 15)

    def test_successful_execution_with_logger(self):
        """Тест успешного выполнения с logging.Logger"""
        # Создаем простой логгер
        test_logger = logging.getLogger('simple_test')

        # Используем декоратор logger с параметром handle
        @logger(handle=test_logger)
        def greet(name):
            return f"Hello, {name}"

        result = greet("World")
        self.assertEqual(result, "Hello, World")

    def test_error_logging(self):
        """Тест логирования ошибок RequestException"""

        # Используем декоратор logger для функции с ошибкой
        @logger
        def failing_function():
            raise requests.exceptions.ConnectionError("Test connection error")

        # Проверяем, что исключение пробрасывается через декоратор
        with self.assertRaises(requests.exceptions.ConnectionError):
            failing_function()

    def test_function_metadata_preserved(self):
        """Тест сохранения имени и документации функции"""

        # Применяем декоратор logger к тестовой функции
        @logger
        def example_function(x):
            """Пример функции с документацией"""
            return x * 2

        # Проверяем, что декоратор сохранил метаданные
        self.assertEqual(example_function.__name__, "example_function")
        self.assertEqual(example_function.__doc__, "Пример функции с документацией")

    def test_decorator_with_parameters(self):
        """Тест декоратора с параметрами"""
        test_logger = logging.getLogger('param_test')

        # Используем декоратор logger с явным указанием handle
        @logger(handle=test_logger)
        def multiply(a, b):
            return a * b

        result = multiply(3, 4)
        self.assertEqual(result, 12)

    def test_decorator_without_parameters(self):
        """Тест декоратора без параметров (простой вызов)"""

        # Используем декоратор logger без скобок
        @logger
        def simple_func():
            return "success"

        result = simple_func()
        self.assertEqual(result, "success")

    def test_function_with_args_and_kwargs(self):
        """Тест функции с позиционными и именованными аргументами"""

        # Декоратор logger должен корректно обрабатывать разные аргументы
        @logger
        def complex_function(a, b, c=0, d=0):
            return a + b + c + d

        result = complex_function(1, 2, c=3, d=4)
        self.assertEqual(result, 10)


class TestLoggerEdgeCases(unittest.TestCase):
    """Тесты граничных случаев для декоратора logger"""

    def test_function_with_no_arguments(self):
        """Тест функции без аргументов"""

        @logger
        def no_args_function():
            return 42

        result = no_args_function()
        self.assertEqual(result, 42)

    def test_function_with_none_return(self):
        """Тест функции, возвращающей None"""

        @logger
        def none_return_function():
            return None

        result = none_return_function()
        self.assertIsNone(result)

    def test_function_with_list_return(self):
        """Тест функции, возвращающей список"""

        @logger
        def list_return_function():
            return [1, 2, 3]

        result = list_return_function()
        self.assertEqual(result, [1, 2, 3])

    def test_function_with_dict_return(self):
        """Тест функции, возвращающей словарь"""

        @logger
        def dict_return_function():
            return {"key": "value"}

        result = dict_return_function()
        self.assertEqual(result, {"key": "value"})

    def test_different_exception_types(self):
        """Тест различных типов исключений RequestException"""

        # Проверяем обработку разных исключений через декоратор logger
        @logger
        def timeout_function():
            raise requests.exceptions.Timeout("Request timed out")

        @logger
        def http_error_function():
            raise requests.exceptions.HTTPError("404 Not Found")

        # Проверяем, что исключения пробрасываются через декоратор
        with self.assertRaises(requests.exceptions.Timeout):
            timeout_function()

        with self.assertRaises(requests.exceptions.HTTPError):
            http_error_function()


# Запуск тестов
if __name__ == "__main__":
    unittest.main(verbosity=2)