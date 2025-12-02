# Импортируем модуль для работы с системными функциями
import sys
# Импортируем модуль для работы с функциями и декораторами
import functools
# Импортируем модуль для логирования
import logging
# Импортируем исключения из модуля requests
import requests.exceptions


# Объявляем функцию декоратора с параметрами
def logger(func=None, *, handle=sys.stdout):
    # Проверяем, передана ли функция в декоратор
    if func is None:
        # Если функция не передана, возвращаем лямбда-функцию
        return lambda func: logger(func, handle=handle)

    # Применяем декоратор functools.wraps для сохранения метаданных
    @functools.wraps(func)
    # Объявляем внутреннюю функцию-обертку
    def inner(*args, **kwargs):
        # Проверяем, является ли handle объектом logging.Logger
        if isinstance(handle, logging.Logger):
            # Если да, используем метод info() для логирования начала
            handle.info(f"Начать {func.__name__} с аргументами: {args}, {kwargs}")
        else:
            # Если нет, используем write() для записи в поток
            handle.write(f"INFO: Начать {func.__name__} с аргументами: {args}, {kwargs}")
            # Принудительно сбрасываем буфер записи
            handle.flush()

        # Начинаем блок обработки исключений
        try:
            # Вызываем оригинальную функцию с аргументами
            res = func(*args, **kwargs)

            # Проверяем тип handle для логирования успеха
            if isinstance(handle, logging.Logger):
                # Используем info() для логирования успешного выполнения
                handle.info(f"Успех {func.__name__}. Результат: {res}")
            else:
                # Используем write() для записи успешного выполнения
                handle.write(f"INFO: Успех {func.__name__}. Результат: {res}")
                # Принудительно сбрасываем буфер записи
                handle.flush()

            # Возвращаем результат оригинальной функции
            return res

        # Обрабатываем все исключения
        except Exception as e:
            # Проверяем тип handle для логирования ошибки
            if isinstance(handle, logging.Logger):
                # Используем error() для логирования ошибки
                handle.error(f"Ошибка в {func.__name__}: {type(e).__name__}: {str(e)}")
            else:
                # Используем write() для записи ошибки
                handle.write(f"ERROR: Ошибка в {func.__name__}: {type(e).__name__}: {str(e)}\n")
                # Принудительно сбрасываем буфер записи
                handle.flush()
            # Повторно вызываем исключение
            raise

    # Возвращаем функцию-обертку
    return inner