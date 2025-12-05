import unittest
# Импортируем все тестируемые классы из модуля models
from models import Author, App, User, Currency, UserCurrency


class TestAuthor(unittest.TestCase):
    """
    Тестирование класса Author (Автор).
    Проверяет корректность работы инициализации, геттеров и сеттеров.
    """

    def setUp(self):
        """
        Метод, выполняемый перед каждым тестом.
        Создает экземпляр Author для тестирования.
        """
        self.author = Author("Тестовое Имя", "P3121")

    def test_initialization(self):
        """
        Тест инициализации объекта Author.
        Проверяет, что значения корректно устанавливаются при создании.
        """
        # Проверяем, что имя установлено корректно
        self.assertEqual(self.author.name, "Тестовое Имя")
        # Проверяем, что группа установлена корректно
        self.assertEqual(self.author.group, "P3121")

    def test_name_setter_valid(self):
        """
        Тест корректного изменения имени через сеттер.
        Проверяет, что имя можно изменить на допустимое значение.
        """
        # Устанавливаем новое имя
        self.author.name = "Новое Имя"
        # Проверяем, что имя изменилось
        self.assertEqual(self.author.name, "Новое Имя")

    def test_name_setter_invalid_type(self):
        """
        Тест некорректного типа данных при изменении имени.
        Ожидается выброс ValueError при передаче не строки.
        """
        # Пытаемся установить имя как число (недопустимый тип)
        with self.assertRaises(ValueError):
            self.author.name = 123

    def test_name_setter_short_name(self):
        """
        Тест слишком короткого имени.
        Ожидается выброс ValueError при имени короче 2 символов.
        """
        # Пытаемся установить имя из одного символа
        with self.assertRaises(ValueError):
            self.author.name = "А"

    def test_group_setter_valid(self):
        """
        Тест корректного изменения группы.
        Проверяет, что группу можно изменить на допустимое значение.
        """
        # Устанавливаем новую группу длиной 5 символов
        self.author.group = "P3122"  # Изменено на длину 5
        # Проверяем, что группа изменилась
        self.assertEqual(self.author.group, "P3122")

    def test_group_setter_invalid_type(self):
        """
        Тест некорректного типа данных при изменении группы.
        Ожидается выброс ValueError при передаче не строки.
        """
        # Пытаемся установить группу как число
        with self.assertRaises(ValueError):
            self.author.group = 12345

    def test_group_setter_short_group(self):
        """
        Тест слишком короткой группы.
        Ожидается выброс ValueError при группе короче 4 символов.
        """
        # Пытаемся установить группу из 3 символов
        with self.assertRaises(ValueError):
            self.author.group = "123"  # Длина 3 < 5


class TestApp(unittest.TestCase):
    """
    Тестирование класса App (Приложение).
    Проверяет корректность работы приложения и его свойств.
    """

    def setUp(self):
        """
        Метод, выполняемый перед каждым тестом.
        Создает экземпляры Author и App для тестирования.
        """
        # Создаем автора с группой длиной 6 символов
        self.author = Author("Автор", "P31211")
        # Создаем приложение с тестовыми данными
        self.app = App("Тестовое приложение", "1.0", self.author)

    def test_initialization(self):
        """
        Тест инициализации объекта App.
        Проверяет, что все свойства установлены корректно.
        """
        # Проверяем название приложения
        self.assertEqual(self.app.name, "Тестовое приложение")
        # Проверяем версию приложения
        self.assertEqual(self.app.version, "1.0")
        # Проверяем, что автор установлен корректно
        self.assertEqual(self.app.author, self.author)

    def test_name_setter_valid(self):
        """
        Тест корректного изменения названия приложения.
        Использует сеттер name_app (специфичное имя в вашей реализации).
        """
        # Изменяем название приложения через сеттер name_app
        self.app.name_app = "Новое название"
        # Проверяем, что название изменилось
        self.assertEqual(self.app.name, "Новое название")

    def test_name_setter_invalid_empty(self):
        """
        Тест пустого названия приложения.
        Ожидается выброс ValueError при пустой строке.
        """
        # Пытаемся установить пустое название
        with self.assertRaises(ValueError):
            self.app.name_app = ""

    def test_name_setter_invalid_type(self):
        """
        Тест некорректного типа данных для названия.
        Ожидается выброс ValueError при передаче не строки.
        """
        # Пытаемся установить название как число
        with self.assertRaises(ValueError):
            self.app.name_app = 123

    def test_version_setter_valid(self):
        """
        Тест корректного изменения версии приложения.
        """
        # Изменяем версию приложения
        self.app.version = "2.0"
        # Проверяем, что версия изменилась
        self.assertEqual(self.app.version, "2.0")

    def test_version_setter_invalid_empty(self):
        """
        Тест пустой версии приложения.
        Ожидается выброс ValueError при пустой строке.
        """
        # Пытаемся установить пустую версию
        with self.assertRaises(ValueError):
            self.app.version = ""

    def test_author_setter_valid(self):
        """
        Тест корректного изменения автора приложения.
        """
        # Создаем нового автора
        new_author = Author("Другой Автор", "P31222")
        # Устанавливаем нового автора
        self.app.author = new_author
        # Проверяем, что автор изменился
        self.assertEqual(self.app.author, new_author)

    def test_author_setter_invalid(self):
        """
        Тест некорректного типа данных для автора.
        Ожидается выброс ValueError при передаче не объекта Author.
        """
        # Пытаемся установить автора как строку
        with self.assertRaises(ValueError):
            self.app.author = "Не автор"


class TestCurrency(unittest.TestCase):
    """
    Тестирование класса Currency (Валюта).
    Проверяет корректность работы валюты и всех ее свойств.
    """

    def setUp(self):
        """
        Метод, выполняемый перед каждым тестом.
        Создает экземпляр Currency с тестовыми данными.
        """
        # Создаем валюту USD с тестовыми данными
        self.currency = Currency(
            id=1,  # Идентификатор валюты
            num_code=840,  # Цифровой код USD
            char_code="USD",  # Символьный код USD
            name="Доллар США",  # Название валюты
            value=75.50,  # Курс валюты
            nominal=1  # Номинал
        )

    def test_initialization(self):
        """
        Тест инициализации объекта Currency.
        Проверяет, что все свойства установлены корректно.
        """
        # Проверяем все свойства валюты
        self.assertEqual(self.currency.id, 1)
        self.assertEqual(self.currency.num_code, 840)
        self.assertEqual(self.currency.char_code, "USD")
        self.assertEqual(self.currency.name, "Доллар США")
        self.assertEqual(self.currency.value, 75.50)
        self.assertEqual(self.currency.nominal, 1)

    def test_id_setter_invalid_negative(self):
        """
        Тест отрицательного ID валюты.
        Ожидается выброс ValueError при отрицательном значении.
        """
        # Пытаемся установить отрицательный ID
        with self.assertRaises(ValueError):
            self.currency.id = -1

    def test_num_code_setter_valid(self):
        """
        Тест корректного изменения цифрового кода валюты.
        """
        # Изменяем цифровой код на код евро
        self.currency.num_code = 978
        # Проверяем, что код изменился
        self.assertEqual(self.currency.num_code, 978)

    def test_num_code_setter_invalid_range(self):
        """
        Тест некорректного диапазона цифрового кода.
        Проверяет граничные значения (меньше 1 и больше 999).
        """
        # Пытаемся установить код 0 (ниже допустимого)
        with self.assertRaises(ValueError):
            self.currency.num_code = 0
        # Пытаемся установить код 1000 (выше допустимого)
        with self.assertRaises(ValueError):
            self.currency.num_code = 1000

    def test_char_code_setter_valid(self):
        """
        Тест корректного изменения символьного кода валюты.
        """
        # Изменяем символьный код на EUR
        self.currency.char_code = "EUR"
        # Проверяем, что код изменился
        self.assertEqual(self.currency.char_code, "EUR")

    def test_char_code_setter_invalid_length(self):
        """
        Тест некорректной длины символьного кода.
        Проверяет, что код должен быть ровно 3 символа.
        """
        # Пытаемся установить код из 2 символов
        with self.assertRaises(ValueError):
            self.currency.char_code = "US"
        # Пытаемся установить код из 4 символов
        with self.assertRaises(ValueError):
            self.currency.char_code = "USDX"

    def test_value_setter_valid(self):
        """
        Тест корректного изменения курса валюты.
        """
        # Изменяем курс валюты
        self.currency.value = 80.25
        # Проверяем, что курс изменился
        self.assertEqual(self.currency.value, 80.25)

    def test_value_setter_invalid_type(self):
        """
        Тест некорректного типа данных для курса валюты.
        Ожидается выброс ValueError при передаче не числа с плавающей точкой.
        """
        # Пытаемся установить курс как строку
        with self.assertRaises(ValueError):
            self.currency.value = "не число"

    def test_nominal_setter_valid(self):
        """
        Тест корректного изменения номинала валюты.
        """
        # Изменяем номинал на 100 (например, для японской иены)
        self.currency.nominal = 100
        # Проверяем, что номинал изменился
        self.assertEqual(self.currency.nominal, 100)

    def test_nominal_setter_invalid(self):
        """
        Тест некорректных значений номинала.
        Проверяет, что номинал должен быть положительным целым числом.
        """
        # Пытаемся установить номинал 0
        with self.assertRaises(ValueError):
            self.currency.nominal = 0
        # Пытаемся установить отрицательный номинал
        with self.assertRaises(ValueError):
            self.currency.nominal = -10


class TestUser(unittest.TestCase):
    """
    Тестирование класса User (Пользователь).
    Проверяет корректность работы пользователя и его свойств.
    """

    def setUp(self):
        """
        Метод, выполняемый перед каждым тестом.
        Создает экземпляр User для тестирования.
        """
        # Создаем пользователя с тестовыми данными
        self.user = User(1, "Иван Иванов")

    def test_initialization(self):
        """
        Тест инициализации объекта User.
        Проверяет, что ID и имя установлены корректно.
        """
        # Проверяем ID пользователя
        self.assertEqual(self.user.id, 1)
        # Проверяем имя пользователя
        self.assertEqual(self.user.name, "Иван Иванов")

    def test_id_setter_valid(self):
        """
        Тест корректного изменения ID пользователя.
        """
        # Изменяем ID пользователя
        self.user.id = 5
        # Проверяем, что ID изменился
        self.assertEqual(self.user.id, 5)

    def test_id_setter_invalid_negative(self):
        """
        Тест отрицательного ID пользователя.
        Ожидается выброс ValueError при отрицательном значении.
        """
        # Пытаемся установить отрицательный ID
        with self.assertRaises(ValueError):
            self.user.id = -1

    def test_id_setter_invalid_zero(self):
        """
        Тест нулевого ID пользователя.
        Ожидается выброс ValueError при значении 0.
        """
        # Пытаемся установить ID = 0
        with self.assertRaises(ValueError):
            self.user.id = 0


class TestUserCurrency(unittest.TestCase):
    """
    Тестирование класса UserCurrency (Связь пользователь-валюта).
    Проверяет корректность работы связи между пользователями и валютами.
    """

    def setUp(self):
        """
        Метод, выполняемый перед каждым тестом.
        Создает экземпляр UserCurrency для тестирования.
        """
        # Создаем связь: ID=1, user_id=1, currency_id=1
        self.user_currency = UserCurrency(1, 1, 1)

    def test_initialization(self):
        """
        Тест инициализации объекта UserCurrency.
        Проверяет, что все ID установлены корректно.
        """
        # Проверяем ID связи
        self.assertEqual(self.user_currency.id, 1)
        # Проверяем ID пользователя
        self.assertEqual(self.user_currency.user_id, 1)
        # Проверяем ID валюты
        self.assertEqual(self.user_currency.currency_id, 1)

    def test_all_setters_valid(self):
        """
        Тест корректного изменения всех свойств связи.
        """
        # Изменяем все ID связи
        self.user_currency.id = 2
        self.user_currency.user_id = 3
        self.user_currency.currency_id = 4

        # Проверяем, что все ID изменились
        self.assertEqual(self.user_currency.id, 2)
        self.assertEqual(self.user_currency.user_id, 3)
        self.assertEqual(self.user_currency.currency_id, 4)

    def test_setters_invalid_negative(self):
        """
        Тест отрицательных значений для всех ID.
        Ожидается выброс ValueError для всех отрицательных значений.
        """
        # Пытаемся установить отрицательный ID связи
        with self.assertRaises(ValueError):
            self.user_currency.id = -1
        # Пытаемся установить отрицательный ID пользователя
        with self.assertRaises(ValueError):
            self.user_currency.user_id = -1
        # Пытаемся установить отрицательный ID валюты
        with self.assertRaises(ValueError):
            self.user_currency.currency_id = -1


if __name__ == '__main__':
    # Запускаем все тесты из модуля
    unittest.main()