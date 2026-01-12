**Лабораторная работа 9. CRUD для приложения отслеживания курсов валют c SQLite базой данных**

**2.2 Цель работы**
1.  Реализовать CRUD (Create, Read, Update, Delete) для сущностей бизнес-логики приложения.
2.  Освоить работу с SQLite в памяти (:memory:) через модуль sqlite3.
3.  Понять принципы первичных и внешних ключей и их роль в связях между таблицами.
4.  Выделить контроллеры для работы с БД и для рендеринга страниц в отдельные модули.
5.  Использовать архитектуру MVC и соблюдать разделение ответственности.
6.  Отображать пользователям таблицу с валютами, на которые они подписаны.
7.  Реализовать полноценный роутер, который обрабатывает GET-запросы и выполняет сохранение/обновление данных и рендеринг страниц.
8.  Научиться тестировать функционал на примере сущностей currency и user с использованием unittest.mock.
9. **Описание моделей, их свойств и связей**

**2.1 Основные сущности**

**Модель Currency (Валюта):**

- **id** - уникальный идентификатор валюты (первичный ключ)
- **num_code** - цифровой код валюты (3 цифры)
- **char_code** - символьный код валюты (3 символа)
- **name** - название валюты
- **value** - текущий курс валюты
- **nominal** - номинал валюты

**Модель User (Пользователь):**

- **id** - уникальный идентификатор пользователя (первичный ключ)
- **name** - имя пользователя

**Модель UserCurrency (Связь пользователя с валютой):**

- **id** - уникальный идентификатор связи
- **user_id** - идентификатор пользователя (внешний ключ)
- **currency_id** - идентификатор валюты (внешний ключ)

**Модель Author (Автор приложения):**

- **name** - имя автора
- **group** - учебная группа автора

**Модель App (Приложение):**

- **name** - название приложения
- **version** - версия приложения
- **author** - автор приложения

**2.2 Связи между таблицами**

1.  Таблица user_currency связывает пользователей с валютами через внешние ключи
2.  Один пользователь может отслеживать несколько валют (связь "один-ко-многим")
3.  Одна валюта может быть отслеживаема несколькими пользователями (связь "многие-ко-многим")

1.  **Структура проекта с назначением файлов**

myapp/

├── controllers/ # Контроллеры (C в MVC)

│ ├── \__init_\_.py # Инициализация контроллеров

│ ├── currencycontroller.py # Контроллер для работы с валютами

│ ├── databasecontroller.py # Контроллер для работы с БД

│ └── pages.py # Контроллер для рендеринга страниц

├── models/ # Модели (M в MVC)

│ ├── \__init_\_.py # Инициализация моделей

│ ├── app.py # Модель приложения

│ ├── author.py # Модель автора

│ ├── currency.py # Модель валюты

│ ├── user.py # Модель пользователя

│ └── user_currency.py # Модель связи пользователь-валюта

├── templates/ # Представления (V в MVC)

│ ├── author.html # Страница "Об авторе"

│ ├── currencies.html # Страница со списком валют

│ ├── index.html # Главная страница

│ ├── user.html # Страница пользователя

│ └── users.html # Страница со списком пользователей

└── myapp.py # Основной файл приложения

1.  **Реализация CRUD с примерами SQL-запросов**
    1.  **Create (Создание)**

def \_create(self) -> None:  
_"""Заполняет базу данных тестовыми данными."""  
_\# Параметры для вставки тестовых пользователей  
users_params = \[  
{"name": "Кристина Лыскова"},  
{"name": "Елизавета Сунгуртян"},  
{"name": "Марина Максименко"},  
{"name": "Анастасия Ромова"},  
{"name": "Анна Кирьянова"},  
{"name": "Вероника Постникова"},  
{"name": "Марк Романов"},  
{"name": "Камилла Курабнова"},  
{"name": "Илья Спиридонов"}  
\]  
\# SQL-запрос для вставки пользователей с именованными параметрами  
users_sql = "INSERT INTO user (name) VALUES (:name)"  
\# Выполняем множественную вставку пользователей  
self.\__cursor.executemany(users_sql, users_params)  
<br/>\# Параметры для вставки тестовых валют  
cur_params = \[  
{"num_code": "840", "char_code": "USD", "name": "Доллар США", "value": 90.0, "nominal": 1},  
{"num_code": "978", "char_code": "EUR", "name": "Евро", "value": 91.0, "nominal": 1},  
{"num_code": "826", "char_code": "GBP", "name": "Фунт стерлингов", "value": 100.0, "nominal": 1},  
{"num_code": "986", "char_code": "BRL", "name": "Бразильский реал", "value": 16.5, "nominal": 1},  
{"num_code": "356", "char_code": "INR", "name": "Индийская рупия", "value": 1.1, "nominal": 100},  
{"num_code": "124", "char_code": "CAD", "name": "Канадский доллар", "value": 65.0, "nominal": 1},  
{"num_code": "756", "char_code": "CHF", "name": "Швейцарский франк", "value": 102.0, "nominal": 1},  
{"num_code": "156", "char_code": "CNY", "name": "Китайский юань", "value": 12.5, "nominal": 10},  
{"num_code": "392", "char_code": "JPY", "name": "Японская иена", "value": 0.6, "nominal": 100}  
\]  
\# SQL-запрос для вставки валют с именованными параметрами  
cur_sqlquery = "INSERT INTO currency(num_code, char_code, name, value, nominal) VALUES(:num_code, :char_code, :name, :value, :nominal)"  
\# Выполняем множественную вставку валют  
self.\__cursor.executemany(cur_sqlquery, cur_params)  
\# Фиксируем изменения в БД  
self.\__con.commit()  
<br/>\# Параметры для создания связей между пользователями и валютами  
user_currency_params = \[  
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
\]  
\# SQL-запрос для вставки связей  
user_currency_sql = "INSERT INTO user_currency (user_id, currency_id) VALUES (:user_id, :currency_id)"  
\# Выполняем множественную вставку связей  
self.\__cursor.executemany(user_currency_sql, user_currency_params)  
\# Фиксируем изменения в БД  
self.\__con.commit()

**4.2 Read (Чтение)**

def \_read(self, cur_code: Optional\[str\] = None, user_id: Optional\[int\] = None, get_users: bool = False) -> List\[  
Dict\[str, Any\]\]:  
_"""  
Читает данные из базы данных с различными фильтрами.  
<br/>Аргументы:  
cur_code: Символьный код валюты для фильтрации  
user_id: ID пользователя для получения его валют  
get_users: Если True, возвращает пользователей вместо валют  
<br/>Возвращает:  
Список словарей с данными из БД  
"""  
_\# Проверяем, запрашиваем ли мы пользователей  
if get_users:  
\# Выполняем запрос на получение всех пользователей  
cur = self.\__con.execute("SELECT \* FROM user")  
result = \[\]  
\# Преобразуем каждую строку результата в словарь  
for \_row in cur:  
result.append({  
'id': \_row\[0\], # ID пользователя  
'name': \_row\[1\] # Имя пользователя  
})  
return result  
\# Проверяем, запрашиваем ли валюты конкретного пользователя  
elif user_id:  
\# SQL-запрос с JOIN для получения валют пользователя  
sql = """  
SELECT c.\* FROM currency c  
JOIN user_currency uc ON c.id = uc.currency_id  
WHERE uc.user_id = ?  
"""  
\# Выполняем запрос с параметром user_id  
cur = self.\__con.execute(sql, (user_id,))  
\# Проверяем, запрашиваем ли конкретную валюту по коду  
elif cur_code:  
\# SQL-запрос для получения валюты по символьному коду  
sql = "SELECT \* FROM currency WHERE char_code = ?"  
\# Выполняем запрос с параметром cur_code  
cur = self.\__con.execute(sql, (cur_code,))  
\# Если фильтров нет, получаем все валюты  
else:  
\# SQL-запрос для получения всех валют  
cur = self.\__con.execute("SELECT \* FROM currency")  
<br/>result = \[\]  
\# Преобразуем каждую строку результата в словарь  
for \_row in cur:  
result.append({  
'id': \_row\[0\], # ID валюты  
'num_code': \_row\[1\], # Цифровой код  
'char_code': \_row\[2\], # Символьный код  
'name': \_row\[3\], # Название валюты  
'value': \_row\[4\], # Текущий курс  
'nominal': \_row\[5\] # Номинал  
})  
return result

**4.3 Update (Обновление)**

def \_update(self, updates: Dict\[str, float\]) -> None:  
_"""  
Обновляет курс валюты.  
<br/>Аргументы:  
updates: Словарь {код_валюты: новое_значение}  
"""  
_\# Проверяем, что есть что обновлять  
if updates:  
\# Извлекаем код валюты из словаря  
cur_code = list(updates.keys())\[0\]  
\# Извлекаем новое значение курса  
new_value = list(updates.values())\[0\]  
\# SQL-запрос для обновления курса валюты  
sql = "UPDATE currency SET value = ? WHERE char_code = ?"  
\# Выполняем запрос с параметрами  
self.\__cursor.execute(sql, (new_value, cur_code))  
\# Фиксируем изменения в БД  
self.\__con.commit()

**4.4 Delete (Удаление)**

def \_delete(self, currency_id: int) -> None:  
_"""  
Удаляет валюту по ID.  
Удаляет все связи с пользователями.  
<br/>Аргументы:  
currency_id: ID удаляемой валюты  
"""  
_\# SQL-запрос для удаления связей с пользователями  
delete_relations_sql = "DELETE FROM user_currency WHERE currency_id = ?"  
\# Выполняем удаление связей  
self.\__cursor.execute(delete_relations_sql, (currency_id,))  
<br/>\# SQL-запрос для удаления самой валюты  
sql = "DELETE FROM currency WHERE id = ?"  
\# Выполняем удаление валюты  
self.\__cursor.execute(sql, (currency_id,))  
\# Фиксируем изменения в БД  
self.\__con.commit()

1.  **Скриншоты работы приложения (главная страница, таблица валют, обновление и удаление)**

Рисунок 1: Главная страница

 Рисунок 2: Таблица валют

Рисунок 3: Удаление валют

Рисунок 4: Таблица валют в консоли

Рисунок 5: Обновление валют

1.  **Примеры тестов с unittest.mock и результаты их выполнения**

- 1.  **Тестирование**

- 1.  _Тест получения списка валют_

def test_list_currencies(self):  
_"""Тест получения списка валют."""  
_\# Создаем мок-объект базы данных  
mock_db = MagicMock()  
mock_db.\_read.return_value = \[{"id": 1, "char_code": "USD", "value": 90}\]  
<br/>\# Создаём контроллер с мок-базой  
controller = CurrencyController(mock_db)  
<br/>\# Вызываем тестируемый метод  
result = controller.list_currencies()  
<br/>\# Проверяем результат  
self.assertEqual(result\[0\]\['char_code'\], "USD")  
self.assertEqual(result\[0\]\['id'\], 1)  
mock_db.\_read.assert_called_once()

_Цель:_ Проверить корректность получения данных из БД

_Результат:_ Успешное получение тестовых данных, проверка структуры

- 1.  _Тест обновления курса валюты_

_"""Тест обновления курса валюты."""  
_mock_db = MagicMock()  
controller = CurrencyController(mock_db)  
<br/>\# Обновляем курс USD  
controller.update_currency("USD", 95.5)  
<br/>\# Проверяем, что метод \_update был вызван с правильными аргументами  
mock_db.\_update.assert_called_once_with({"USD": 95.5})

_Цель:_ Проверить передачу параметров обновления

_Результат:_ Параметры переданы корректно в метод БД

- 1.  _Тест удаления валюты по ID_

def test_delete_currency(self):  
_"""Тест удаления валюты по ID."""  
_mock_db = MagicMock()  
controller = CurrencyController(mock_db)  
<br/>\# Удаляем валюту с ID 3  
controller.delete_currency(3)  
<br/>\# Проверяем вызов метода удаления  
mock_db.\_delete.assert_called_once_with(3)

_Цель:_ Проверить удаление по идентификатору

_Результат:_ Метод удаления вызван с правильным ID

- 1.  _Тест обновления курсов разных валют_

def test_update_currency_with_different_codes(self):  
_"""Тест обновления курсов разных валют."""  
_mock_db = MagicMock()  
controller = CurrencyController(mock_db)  
<br/>\# Обновляем несколько валют  
controller.update_currency("USD", 92.0)  
controller.update_currency("EUR", 88.5)  
controller.update_currency("CNY", 12.8)  
<br/>\# Проверяем, что метод вызывался 3 раза с правильными параметрами  
self.assertEqual(mock_db.\_update.call_count, 3)  
<br/>\# Получаем все вызовы  
calls = mock_db.\_update.call_args_list  
<br/>\# Проверяем параметры каждого вызова  
self.assertEqual(calls\[0\]\[0\]\[0\], {"USD": 92.0})  
self.assertEqual(calls\[1\]\[0\]\[0\], {"EUR": 88.5})  
self.assertEqual(calls\[2\]\[0\]\[0\], {"CNY": 12.8})

_Цель:_ Проверить множественные обновления

_Результат:_ Все валюты обновлены с правильными параметрами

- 1.  _Тест получения списка всех пользователей_

def test_get_users(self):  
_"""Тест получения списка всех пользователей."""  
_mock_db = MagicMock()  
\# Настраиваем мок для возврата тестовых данных  
test_users = \[  
{"id": 1, "name": "Кристина Лыскова"},  
{"id": 2, "name": "Елизавета Сунгуртян"},  
{"id": 3, "name": "Марина Максименко"}  
\]  
mock_db.\_read.return_value = test_users  
controller = CurrencyController(mock_db)  
<br/>\# Получаем список пользователей  
result = controller.get_users()  
<br/>\# Проверяем результат  
self.assertEqual(len(result), 3)  
self.assertEqual(result\[0\]\['name'\], "Кристина Лыскова")  
self.assertEqual(result\[1\]\['id'\], 2)  
\# Проверяем, что метод вызван с флагом get_users=True  
mock_db.\_read.assert_called_once_with(get_users=True)

_Цель:_ Проверить получение данных пользователей

_Результат:_ Список пользователей получен, флаг установлен корректно

- 1.  _Тест получения валют пользователя_

def test_get_user_currencies(self):  
_"""Тест получения валют пользователя."""  
_mock_db = MagicMock()  
\# Настраиваем мок для возврата тестовых данных  
test_data = \[  
{"id": 1, "char_code": "USD", "name": "Доллар США", "value": 90.0, "num_code": "840", "nominal": 1},  
{"id": 2, "char_code": "EUR", "name": "Евро", "value": 95.5, "num_code": "978", "nominal": 1}  
\]  
mock_db.\_read.return_value = test_data  
controller = CurrencyController(mock_db)  
<br/>\# Получаем валюты пользователя с ID 5  
result = controller.get_user_currencies(5)  
<br/>\# Проверяем результат  
self.assertEqual(len(result), 2)  
self.assertEqual(result\[0\]\['char_code'\], "USD")  
self.assertEqual(result\[1\]\['name'\], "Евро")  
\# Проверяем, что метод вызван с правильным user_id  
mock_db.\_read.assert_called_once_with(user_id=5)

_Цель:_ Проверить фильтрацию валют по пользователю

_Результат_: Валюты пользователя получены, фильтр применён правильно

- 1.  **Результаты тестирования**

Ran 6 tests in 0.010s  
<br/>OK

Все тесты успешно пройдены: контроллер корректно взаимодействует с БД через мок-объекты.

1.  **Выводы**

**1) Применение архитектуры MVC**

В ходе работы успешно применена архитектура MVC, что позволило:

- Чётко разделить ответственность между компонентами приложения
- Упростить поддержку и расширение кода
- Обеспечить переиспользование компонентов

**2) Работа с SQLite**

Освоена работа с SQLite в памяти, включая:

- Создание и управление таблицами с первичными и внешними ключами
- Выполнение параметризованных запросов для защиты от SQL-инъекций
- Организацию связей между таблицами через внешние ключи

**3) Обработка маршрутов и рендеринг шаблонов**

Реализована полноценная маршрутизация HTTP-запросов:

- Обработка различных URL-адресов с помощью простого роутера
- Рендеринг HTML-шаблонов с использованием Jinja2
- Динамическая передача данных из контроллеров в представления

**4) Итоговые достижения**

В результате выполнения работы:

1.  Создано веб-приложение для отслеживания курсов валют
2.  Реализованы все CRUD-операции для сущностей приложения
3.  Организована связь между пользователями и валютами через промежуточную таблицу
4.  Разработана система шаблонов для отображения данных пользователю
5.  Созданы модульные тесты для проверки функциональности контроллеров
