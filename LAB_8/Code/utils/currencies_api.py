# Импортируем библиотеку для выполнения HTTP-запросов
import requests
# Импортируем библиотеку для системных функций
import sys


# Объявляем функцию для получения курсов валют
def get_currencies(currency_codes: list, url: str = "https://www.cbr-xml-daily.ru/daily_json.js",
                   handle=sys.stdout) -> dict:
    """
    Получает курсы валют с API Центробанка России.

    Args:
        currency_codes (list): Список символьных кодов валют (например, ['USD', 'EUR']).

    Returns:
        dict: Словарь, где ключи - символьные коды валют, а значения - их курсы.
              Возвращает None в случае ошибки запроса.
    """

    # Пытаемся выполнить запрос к API
    try:
        # Отправляем GET-запрос по указанному URL
        response = requests.get(url)

        # Проверяем статус ответа (если ошибка - выбросит исключение)
        response.raise_for_status()  # Проверка на ошибки HTTP

    # Если произошла ошибка при запросе (нет интернета, сайт недоступен и т.д.)
    except requests.exceptions.RequestException as e:
        # Выбрасываем своё исключение с сообщением об ошибке
        raise ConnectionError(f"API недоступен: {e}")

    # Пытаемся преобразовать ответ в JSON
    try:
        # Конвертируем ответ сервера в словарь Python
        data = response.json()

    # Если JSON некорректный (битый или невалидный)
    except ValueError as e:
        # Выбрасываем исключение о проблеме с JSON
        raise ValueError("Некорректный JSON")

    # Создаём пустой словарь для хранения результатов
    currencies = {}

    # Проверяем, есть ли в данных ключ "Valute" (где хранятся курсы валют)
    if "Valute" in data:
        # Проходим по каждому коду валюты из списка, который нам передали
        for code in currency_codes:
            # Проверяем, есть ли текущая валюта в данных от API
            if code in data["Valute"]:
                # Достаём значение курса валюты
                value = data["Valute"][code]["Value"]
                # Добавляем валюту и её курс в наш словарь результатов
                currencies[code] = value
            else:
                # Если валюты нет в данных - выбрасываем ошибку
                raise KeyError(f"Валюта '{code}' отсутствует в данных.")

            # Проверяем, что курс является числом (int или float)
            if not (type(value) == int or type(value) == float):
                # Если не число - выбрасываем ошибку
                raise TypeError(f"Курс валюты '{code}' имеет неверный тип: {type(value)}")

    # Если ключа "Valute" вообще нет в ответе API
    else:
        # Выбрасываем ошибку об отсутствии нужного ключа
        raise KeyError("Нет ключа 'Valute'")

    # Возвращаем словарь с курсами валют
    return currencies

