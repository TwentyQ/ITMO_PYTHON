from models import Author, App
from urllib.parse import parse_qs
from http.server import HTTPServer, BaseHTTPRequestHandler
from controllers import CurrencyRatesCRUD, CurrencyController, PagesController
from typing import Dict, List, Any, Optional

# Инициализация контроллеров для работы с данными
db_controller = CurrencyRatesCRUD(None)  # Контроллер для работы с базой данных валют
currency_controller = CurrencyController(db_controller)  # Контроллер бизнес-логики валют
pages_controller = PagesController()  # Контроллер для рендеринга HTML-страниц
db_controller._create()  # Создание необходимых таблиц в базе данных

# Данные об авторе и приложении
main_author = Author('Анастасия Данилова', 'P3121')  # Объект автора с именем и группой
main_app = App("Приложение отслеживания курса валют", "1.0", main_author)  # Объект приложения


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Обработчик HTTP-запросов для сервера отслеживания курса валют.
    """

    def do_GET(self) -> None:
        """
        Обрабатывает GET-запросы к серверу.
        """
        # Выводим путь запроса для отладки
        print(self.path)

        # Разделяем путь и параметры запроса, парсим параметры в словарь
        url_query_dict: Dict[str, List[str]] = parse_qs(self.path.rpartition('?')[-1])
        # Получаем чистый путь без параметров
        path: str = self.path.split('?')[0]

        # Переменная для хранения результата обработки запроса
        result: str = ""

        # Обработка маршрутов
        if path == '/':
            # Главная страница приложения
            # Получаем список всех валют из контроллера
            currencies: List[Dict[str, Any]] = currency_controller.list_currencies()
            # Рендерим главную страницу с передачей всех необходимых данных
            result = pages_controller.render_index(
                currencies,
                main_author.name,
                main_author.group,
                main_app.name,
                main_app.version
            )

        elif path == '/users':
            # Страница со списком пользователей
            # Получаем список пользователей из контроллера
            users: List[Dict[str, Any]] = currency_controller.get_users()
            # Рендерим страницу пользователей
            result = pages_controller.render_users(main_app.name, users)

        elif path == '/user':
            # Страница конкретного пользователя
            # Проверяем наличие параметра id в запросе
            if 'id' in url_query_dict:
                # Извлекаем ID пользователя из параметров запроса
                user_id: int = int(url_query_dict['id'][0])
                # Получаем данные пользователя по ID
                user: Optional[Dict[str, Any]] = currency_controller.get_user(user_id)

                if user:
                    # Если пользователь найден, получаем его валюты
                    user_currencies: List[Dict[str, Any]] = currency_controller.get_user_currencies(user_id)
                    # Рендерим страницу пользователя
                    result = pages_controller.render_user(main_app.name, user, user_currencies)
                else:
                    # Если пользователь не найден, возвращаем сообщение об ошибке
                    result = "Пользователь не найден"
            else:
                # Если ID не указан, возвращаем сообщение об ошибке
                result = "ID пользователя не указан"

        elif path == '/currencies':
            # Страница управления курсами валют
            # Получаем текущий список валют
            currencies: List[Dict[str, Any]] = currency_controller.list_currencies()
            # Сообщение о результате операций с валютами
            result_msg: str = ""

            # Проверяем query-параметры на наличие обновлений курсов
            # Итерируем по всем параметрам запроса
            for param, values in url_query_dict.items():
                # Если параметр состоит из 3 символов (код валюты)
                if len(param) == 3:
                    try:
                        # Пытаемся преобразовать значение в число
                        value: float = float(values[0])
                        # Обновляем курс валюты в базе данных
                        currency_controller.update_currency(param, value)
                        # Формируем сообщение об успешном обновлении
                        result_msg = f"Курс {param} обновлен на {value}"
                    except (ValueError, TypeError):
                        # В случае ошибки преобразования или обновления
                        result_msg = f"Ошибка обновления {param}"

            # Рендерим страницу валют с сообщением о результате операций
            result = pages_controller.render_currencies(main_app.name, currencies, result_msg)

        elif path == '/author':
            # Страница "Об авторе"
            # Рендерим страницу с информацией об авторе
            result = pages_controller.render_author(
                main_author.name,
                main_author.group,
                main_app.name,
                main_app.version
            )

        elif path == '/currencies/delete':
            # Удаление валюты из системы
            # Проверяем наличие параметра id в запросе
            if 'id' in url_query_dict:
                # Извлекаем ID валюты для удаления
                currency_id: int = int(url_query_dict['id'][0])
                # Удаляем валюту через контроллер
                currency_controller.delete_currency(currency_id)
                # Перенаправляем на страницу валют после удаления
                self.send_response(302)  # Код перенаправления
                self.send_header('Location', '/currencies')  # URL для перенаправления
                self.end_headers()
                self.wfile.flush()  # Очищаем буфер записи
                return  # Прерываем выполнение, так как ответ уже отправлен
            else:
                # Если ID не указан, возвращаем сообщение об ошибке
                result = "ID не указан"

        elif path == '/currencies/update':
            # Обновление курса валюты через query-параметры
            result_msg: str = ""

            # Итерируем по всем параметрам запроса
            for param, values in url_query_dict.items():
                # Проверяем, что параметр - это код валюты (3 буквы)
                if len(param) == 3 and param.isalpha():
                    try:
                        # Пытаемся обновить курс валюты
                        value: float = float(values[0])
                        currency_controller.update_currency(param.upper(), value)
                        # Добавляем информацию об успешном обновлении
                        result_msg += f"Курс {param.upper()} обновлён на {value}"
                    except Exception as e:
                        # В случае ошибки добавляем сообщение об ошибке
                        result_msg += f"Ошибка обновления {param.upper()}: {str(e)}"

            # Если не было ни одного обновления
            if not result_msg:
                result_msg = "Не указаны валюты для обновления"

            # Получаем обновленный список валют
            currencies: List[Dict[str, Any]] = currency_controller.list_currencies()
            # Рендерим страницу с результатами обновления
            result = pages_controller.render_currencies(main_app.name, currencies, result_msg)

        elif path == '/currencies/show':
            # Вывод информации о валютах в консоль (для отладки)
            currencies: List[Dict[str, Any]] = currency_controller.list_currencies()
            # Итерируем по всем валютам и выводим их данные
            for currency in currencies:
                print(
                    f"ID: {currency['id']}, "
                    f"Code: {currency['char_code']}, "
                    f"Name: {currency['name']}, "
                    f"Value: {currency['value']}, "
                    f"Nominal: {currency['nominal']}"
                )

        else:
            # Если маршрут не найден, возвращаем сообщение об ошибке 404
            result = "Страница не найдена"

        # Отправляем успешный HTTP-ответ
        self.send_response(200)  # Код успешного выполнения
        self.send_header('Content-Type', 'text/html; charset=utf-8')  # Устанавливаем тип контента
        self.end_headers()  # Завершаем заголовки
        # Отправляем сгенерированный HTML-код клиенту
        self.wfile.write(bytes(result, "utf-8"))


# Создание и запуск HTTP-сервера
httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()