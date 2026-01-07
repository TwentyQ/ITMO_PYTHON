import sqlite3
from typing import Dict, List, Optional, Any


class CurrencyRatesCRUD:
    """
    Класс для CRUD-операций с валютами и пользователями в SQLite.
    Работает с in-memory базой данных.
    """

    def __init__(self, currency_rates_obj: Any) -> None:
        """
        Инициализирует подключение к БД и создаёт таблицы.

        """
        # Подключаемся к in-memory базе данных SQLite
        self.__con = sqlite3.connect(':memory:')
        # Создаем необходимые таблицы в БД
        self.__createtable()
        # Создаем курсор для выполнения SQL-запросов
        self.__cursor = self.__con.cursor()

    def __createtable(self) -> None:
        """Создаёт таблицы в базе данных при инициализации."""
        # Создаем таблицу currency для хранения информации о валютах
        self.__con.execute(
            "CREATE TABLE IF NOT EXISTS currency("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "  # Автоинкрементируемый первичный ключ
            "num_code TEXT NOT NULL,"  # Цифровой код валюты
            "char_code TEXT NOT NULL,"  # Символьный код валюты
            "name TEXT NOT NULL,"  # Название валюты
            "value FLOAT,"  # Текущий курс валюты
            "nominal INTEGER);")  # Номинал валюты

        # Фиксируем создание таблицы
        self.__con.commit()

        # Создаем таблицу user для хранения информации о пользователях
        self.__con.execute(
            "CREATE TABLE IF NOT EXISTS user ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"  # Автоинкрементируемый первичный ключ
            "name TEXT NOT NULL);")  # Имя пользователя
        # Фиксируем создание таблицы
        self.__con.commit()

        # Создаём таблицу связей между пользователями и валютами
        self.__con.execute(
            "CREATE TABLE IF NOT EXISTS user_currency ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"  # Автоинкрементируемый первичный ключ связи
            "user_id INTEGER NOT NULL,"  # ID пользователя
            "currency_id INTEGER NOT NULL,"  # ID валюты
            "FOREIGN KEY(user_id) REFERENCES user(id),"  # Связь с таблицей user
            "FOREIGN KEY(currency_id) REFERENCES currency(id));")  # Связь с таблицей currency
        # Фиксируем создание таблицы связей
        self.__con.commit()

    def _create(self) -> None:
        """Заполняет базу данных тестовыми данными."""
        # Параметры для вставки тестовых пользователей
        users_params = [
            {"name": "Кристина Лыскова"},
            {"name": "Елизавета Сунгуртян"},
            {"name": "Марина Максименко"},
            {"name": "Анастасия Ромова"},
            {"name": "Анна Кирьянова"},
            {"name": "Вероника Постникова"},
            {"name": "Марк Романов"},
            {"name": "Камилла Курабнова"},
            {"name": "Илья Спиридонов"}
        ]
        # SQL-запрос для вставки пользователей с именованными параметрами
        users_sql = "INSERT INTO user (name) VALUES (:name)"
        # Выполняем множественную вставку пользователей
        self.__cursor.executemany(users_sql, users_params)

        # Параметры для вставки тестовых валют
        cur_params = [
            {"num_code": "840", "char_code": "USD", "name": "Доллар США", "value": 90.0, "nominal": 1},
            {"num_code": "978", "char_code": "EUR", "name": "Евро", "value": 91.0, "nominal": 1},
            {"num_code": "826", "char_code": "GBP", "name": "Фунт стерлингов", "value": 100.0, "nominal": 1},
            {"num_code": "986", "char_code": "BRL", "name": "Бразильский реал", "value": 16.5, "nominal": 1},
            {"num_code": "356", "char_code": "INR", "name": "Индийская рупия", "value": 1.1, "nominal": 100},
            {"num_code": "124", "char_code": "CAD", "name": "Канадский доллар", "value": 65.0, "nominal": 1},
            {"num_code": "756", "char_code": "CHF", "name": "Швейцарский франк", "value": 102.0, "nominal": 1},
            {"num_code": "156", "char_code": "CNY", "name": "Китайский юань", "value": 12.5, "nominal": 10},
            {"num_code": "392", "char_code": "JPY", "name": "Японская иена", "value": 0.6, "nominal": 100}
        ]
        # SQL-запрос для вставки валют с именованными параметрами
        cur_sqlquery = "INSERT INTO currency(num_code, char_code, name, value, nominal) VALUES(:num_code, :char_code, :name, :value, :nominal)"
        # Выполняем множественную вставку валют
        self.__cursor.executemany(cur_sqlquery, cur_params)
        # Фиксируем изменения в БД
        self.__con.commit()

        # Параметры для создания связей между пользователями и валютами
        user_currency_params = [
            {"user_id": 1, "currency_id": 1},
            {"user_id": 1, "currency_id": 4},
            {"user_id": 2, "currency_id": 6},
            {"user_id": 2, "currency_id": 9},
            {"user_id": 3, "currency_id": 7},
            {"user_id": 1, "currency_id": 6},
            {"user_id": 4, "currency_id": 8},
            {"user_id": 2, "currency_id": 5},
            {"user_id": 8, "currency_id": 6},
            {"user_id": 7, "currency_id": 1},
            {"user_id": 9, "currency_id": 4},
            {"user_id": 6, "currency_id": 2},
            {"user_id": 5, "currency_id": 4},
            {"user_id": 3, "currency_id": 7},
            {"user_id": 1, "currency_id": 9},
            {"user_id": 4, "currency_id": 1},
            {"user_id": 2, "currency_id": 5},
            {"user_id": 8, "currency_id": 3},
            {"user_id": 7, "currency_id": 5},
            {"user_id": 9, "currency_id": 3},
            {"user_id": 6, "currency_id": 6},
            {"user_id": 5, "currency_id": 8},
        ]
        # SQL-запрос для вставки связей
        user_currency_sql = "INSERT INTO user_currency (user_id, currency_id) VALUES (:user_id, :currency_id)"
        # Выполняем множественную вставку связей
        self.__cursor.executemany(user_currency_sql, user_currency_params)
        # Фиксируем изменения в БД
        self.__con.commit()

    def _read(self, cur_code: Optional[str] = None, user_id: Optional[int] = None, get_users: bool = False) -> List[
        Dict[str, Any]]:
        """
        Читает данные из базы данных с различными фильтрами.

        Аргументы:
            cur_code: Символьный код валюты для фильтрации
            user_id: ID пользователя для получения его валют
            get_users: Если True, возвращает пользователей вместо валют

        Возвращает:
            Список словарей с данными из БД
        """
        # Проверяем, запрашиваем ли мы пользователей
        if get_users:
            # Выполняем запрос на получение всех пользователей
            cur = self.__con.execute("SELECT * FROM user")
            result = []
            # Преобразуем каждую строку результата в словарь
            for _row in cur:
                result.append({
                    'id': _row[0],  # ID пользователя
                    'name': _row[1]  # Имя пользователя
                })
            return result
        # Проверяем, запрашиваем ли валюты конкретного пользователя
        elif user_id:
            # SQL-запрос с JOIN для получения валют пользователя
            sql = """
                SELECT c.* FROM currency c
                JOIN user_currency uc ON c.id = uc.currency_id
                WHERE uc.user_id = ?
            """
            # Выполняем запрос с параметром user_id
            cur = self.__con.execute(sql, (user_id,))
        # Проверяем, запрашиваем ли конкретную валюту по коду
        elif cur_code:
            # SQL-запрос для получения валюты по символьному коду
            sql = "SELECT * FROM currency WHERE char_code = ?"
            # Выполняем запрос с параметром cur_code
            cur = self.__con.execute(sql, (cur_code,))
        # Если фильтров нет, получаем все валюты
        else:
            # SQL-запрос для получения всех валют
            cur = self.__con.execute("SELECT * FROM currency")

        result = []
        # Преобразуем каждую строку результата в словарь
        for _row in cur:
            result.append({
                'id': _row[0],  # ID валюты
                'num_code': _row[1],  # Цифровой код
                'char_code': _row[2],  # Символьный код
                'name': _row[3],  # Название валюты
                'value': _row[4],  # Текущий курс
                'nominal': _row[5]  # Номинал
            })
        return result

    def _update(self, updates: Dict[str, float]) -> None:
        """
        Обновляет курс валюты.

        Аргументы:
            updates: Словарь {код_валюты: новое_значение}
        """
        # Проверяем, что есть что обновлять
        if updates:
            # Извлекаем код валюты из словаря
            cur_code = list(updates.keys())[0]
            # Извлекаем новое значение курса
            new_value = list(updates.values())[0]
            # SQL-запрос для обновления курса валюты
            sql = "UPDATE currency SET value = ? WHERE char_code = ?"
            # Выполняем запрос с параметрами
            self.__cursor.execute(sql, (new_value, cur_code))
            # Фиксируем изменения в БД
            self.__con.commit()

    def _delete(self, currency_id: int) -> None:
        """
        Удаляет валюту по ID.
        Удаляет все связи с пользователями.

        Аргументы:
            currency_id: ID удаляемой валюты
        """
        # SQL-запрос для удаления связей с пользователями
        delete_relations_sql = "DELETE FROM user_currency WHERE currency_id = ?"
        # Выполняем удаление связей
        self.__cursor.execute(delete_relations_sql, (currency_id,))

        # SQL-запрос для удаления самой валюты
        sql = "DELETE FROM currency WHERE id = ?"
        # Выполняем удаление валюты
        self.__cursor.execute(sql, (currency_id,))
        # Фиксируем изменения в БД
        self.__con.commit()
