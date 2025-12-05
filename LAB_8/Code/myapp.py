# Импорт шаблонизатора Jinja2 для работы с HTML-шаблонами
from jinja2 import Environment, PackageLoader, select_autoescape
# Импорт моделей данных приложения
from models import Author, App, User, Currency, UserCurrency
# Импорт функций для парсинга URL
from urllib.parse import urlparse, parse_qs
# Импорт классов для создания HTTP-сервера
from http.server import HTTPServer, BaseHTTPRequestHandler
# Импорт функции для получения курсов валют из API
from utils.currencies_api import get_currencies

# Создание окружения Jinja2 для работы с шаблонами
env = Environment(
    # Загрузчик шаблонов из пакета "myapp"
    loader=PackageLoader("myapp"),
    # Включение автоэкранирования HTML-тегов для безопасности
    autoescape=select_autoescape()
)

# Загрузка HTML-шаблонов из файлов
template_index = env.get_template("index.html")        # Шаблон главной страницы
template_users = env.get_template("users.html")        # Шаблон страницы пользователей
template_user = env.get_template("user.html")          # Шаблон страницы пользователя
template_currencies = env.get_template("currencies.html")  # Шаблон страницы валют
template_author = env.get_template("author.html")      # Шаблон страницы автора

# Создание объекта автора приложения
main_author = Author('Анастасия Данилова', 'P3121')
# Создание объекта приложения
main_app = App("Приложение отслеживания курса валют", "1.0", main_author)

# Список пользователей приложения
users_list = [
    User(1, "Кристина Лыскова"),
    User(2, "Елизавета Сунгуртян"),
    User(3, "Марина Максименко"),
    User(4, "Анастасия Ромова"),
    User(5, "Анна Кирьянова"),
    User(6, "Вероника Постникова"),
    User(7, "Марк Романов"),
    User(8, "Камилла Курабнова"),
    User(9, "Илья Спиридонов")
]

# Список валют с начальными курсами
currencies_list = [
    Currency(1, 840, "USD", "Доллар США", 90.0, 1),
    Currency(2, 978, "EUR", "Евро", 91.0, 1),
    Currency(3, 826, "GBP", "Фунт стерлингов", 100.0, 1),
    Currency(4, 986, "BRL", "Бразильский реал", 16.5, 1),
    Currency(5, 356, "INR", "Индийская рупия", 1.1, 100),
    Currency(6, 124, "CAD", "Канадский доллар", 65.0, 1),
    Currency(7, 756, "CHF", "Швейцарский франк", 102.0, 1),
    Currency(8, 156, "CNY", "Китайский юань", 12.5, 10),
    Currency(9, 392, "JPY", "Японская иена", 0.6, 100)
]

# Список связей между пользователями и отслеживаемыми валютами
user_currencies_list = [
    UserCurrency(1, 1, 1),
    UserCurrency(2, 1, 4),
    UserCurrency(3, 2, 6),
    UserCurrency(4, 2, 9),
    UserCurrency(5, 3, 7),
    UserCurrency(6, 1, 6),
    UserCurrency(7, 4, 8),
    UserCurrency(8, 2, 5),
    UserCurrency(9, 8, 6),
    UserCurrency(10, 7, 1),
    UserCurrency(11, 9, 4),
    UserCurrency(12, 6, 2),
    UserCurrency(13, 5, 4),
    UserCurrency(14, 3, 7),
    UserCurrency(15, 1, 9),
    UserCurrency(16, 4, 1),
    UserCurrency(17, 2, 5),
    UserCurrency(18, 8, 3),
    UserCurrency(19, 7, 5),
    UserCurrency(20, 9, 3),
    UserCurrency(21, 6, 6),
    UserCurrency(22, 5, 8)
]


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Обработчик HTTP-запросов для веб-сервера.

    Методы:
        do_GET(): Обрабатывает HTTP GET-запросы
        _update_currency_rates(): Обновляет курсы валют из внешнего API
    """

    def do_GET(self):
        """Обрабатывает GET-запросы и возвращает соответствующие HTML-страницы."""
        # Объявление глобальных переменных шаблонов для использования внутри метода
        global template_index, template_users, template_user, template_currencies, template_author

        # Установка HTTP-статуса 200 (OK)
        self.send_response(200)
        # Установка заголовка Content-Type с указанием кодировки UTF-8
        self.send_header('Content-Type', 'text/html; charset=utf-8')

        # Вывод пути запроса в консоль для отладки
        print(self.path)
        # Парсинг параметров запроса из URL
        # rpartition('?') разделяет строку по последнему '?' и возвращает 3 части
        # parse_qs преобразует строку параметров в словарь
        url_query_dict = parse_qs(self.path.rpartition('?')[-1])

        # Создание базового словаря данных для передачи в шаблоны
        base_data = {
            'myapp': "Приложение отслеживания курса валют",  # Название приложения
            'navigation': [  # Меню навигации
                {'caption': 'Главная страница', 'href': "/"},
                {'caption': 'Пользователи', 'href': "/users"},
                {'caption': 'Курсы валют', 'href': "/currencies"},
                {'caption': 'Об авторе', 'href': "/author"}
            ],
            'author_name': main_author.name,  # Имя автора
            'group': main_author.group,        # Группа автора
            'app_name': main_app.name,         # Название приложения
            'version': main_app.version,       # Версия приложения
        }

        # Маршрутизация по пути запроса
        # Главная страница
        if self.path == '/':
            # Рендеринг главной страницы с базовыми данными
            result = template_index.render(**base_data)

        # Страница списка пользователей
        elif '/users' in self.path:
            # Добавление списка пользователей в данные
            base_data['users'] = users_list
            # Рендеринг страницы пользователей
            result = template_users.render(**base_data)

        # Страница конкретного пользователя
        elif '/user' in self.path:
            # Проверка наличия параметра id в запросе
            if 'id' in url_query_dict:
                # Получение id пользователя из параметров запроса
                user_id = int(url_query_dict['id'][0])
                # Поиск пользователя по id в списке пользователей
                # next() возвращает первый элемент, удовлетворяющий условию, или None
                user = next((u for u in users_list if u.id == user_id), None)

                # Если пользователь найден
                if user:
                    # Получение списка id валют, которые отслеживает пользователь
                    user_currency_ids = [uc.currency_id for uc in user_currencies_list if uc.user_id == user_id]
                    # Получение объектов валют по найденным id
                    user_currencies = [c for c in currencies_list if c.id in user_currency_ids]

                    # Добавление данных пользователя и его валют в словарь данных
                    base_data['user'] = user
                    base_data['user_currencies'] = user_currencies
                    # Рендеринг страницы пользователя
                    result = template_user.render(**base_data)
                else:
                    # Если пользователь не найден - перенаправление на главную
                    result = template_index.render(**base_data)
            else:
                # Если параметр id отсутствует - перенаправление на главную
                result = template_index.render(**base_data)

        # Страница курсов валют
        elif '/currencies' in self.path:
            # Обновление курсов валют из API
            self._update_currency_rates()
            # Добавление списка валют в данные
            base_data['currencies'] = currencies_list
            # Рендеринг страницы валют
            result = template_currencies.render(**base_data)

        # Страница об авторе
        elif '/author' in self.path:
            # Рендеринг страницы об авторе
            result = template_author.render(**base_data)

        # Обработка несуществующих маршрутов
        else:
            # Для несуществующих маршрутов возвращается главная страница
            result = template_index.render(**base_data)

        # Завершение заголовков HTTP-ответа
        self.end_headers()
        # Преобразование строки результата в байты и отправка клиенту
        self.wfile.write(bytes(result, "utf-8"))

    def _update_currency_rates(self):
        """Обновляет курсы валют из внешнего API."""
        try:
            # Получение списка символьных кодов всех валют
            currency_codes = [currency.char_code for currency in currencies_list]
            # Запрос актуальных курсов валют из API
            rates = get_currencies(currency_codes)

            # Обновление курсов для каждой валюты
            for currency in currencies_list:
                # Проверка, что валюта есть в полученных данных
                if currency.char_code in rates:
                    # Сохранение старого значения курса для логирования
                    old_value = currency.value
                    # Обновление значения курса в объекте Currency
                    currency.value = rates[currency.char_code]
                    # Вывод информации об обновлении курса в консоль
                    print(f"Обновлен курс {currency.char_code}: {old_value:.2f} -> {currency.value:.2f}")
        except Exception as e:
            # Обработка исключений при обновлении курсов
            print(f"Ошибка при обновлении курсов: {e}")


# Создание HTTP-сервера, слушающего localhost на порту 8080
httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
# Вывод сообщения о запуске сервера
print('server is running')
# Запуск сервера в бесконечном цикле обработки запросов
httpd.serve_forever()