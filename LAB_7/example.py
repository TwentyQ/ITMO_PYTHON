# Импортируем необходимые библиотеки
import logging  # для работы с логированием (запись логов в файл)
import math  # для математических операций (например, вычисление квадратного корня)
from typing import Optional, Tuple  # для указания типов данных (необязательный возврат и кортеж)

# Настраиваем систему логирования
logging.basicConfig(
    filename="quadratic.log",  # указываем файл, куда будут записываться логи
    level=logging.DEBUG,  # устанавливаем минимальный уровень логирования (DEBUG и выше)
    format="%(levelname)s: %(message)s"  # формат записи: УРОВЕНЬ: сообщение
)


# Создаем декоратор для логирования - это обертка вокруг функции
def quadratic_logger(func):  # func - это функция, которую мы будем оборачивать
    def wrapper(a, b, c):  # внутренняя функция-обертка, принимает те же аргументы
        # Логируем начало решения уравнения с уровнем INFO
        logging.info(f"Solving equation: {a}x^2 + {b}x + {c} = 0")

        try:
            # Вызываем оригинальную функцию solve_quadratic
            result = func(a, b, c)

            # Проверяем результат: если None - значит дискриминант < 0
            if result is None:
                # Логируем предупреждение WARNING
                logging.warning("Discriminant < 0: no real roots")
            # Для успешных случаев INFO уже записан в начале

            return result  # возвращаем результат оригинальной функции

        except Exception as e:  # если произошла ошибка
            # Проверяем тип ошибки по тексту сообщения
            if "must be numeric" in str(e):
                # Логируем ошибку ERROR для некорректных типов данных
                logging.error(f"Invalid coefficients: {e}")
            elif "cannot be zero" in str(e):
                # Логируем критическую ошибку CRITICAL для невозможных уравнений
                logging.critical(f"Impossible equation: {e}")
            else:
                # Для всех остальных ошибок используем уровень ERROR
                logging.error(f"Error: {e}")
            raise  # повторно выбрасываем исключение, чтобы программа знала об ошибке

    return wrapper  # возвращаем функцию-обертку


# Основная функция для решения квадратного уравнения
# @quadratic_logger - это применение декоратора (функция оборачивается в логирование)
@quadratic_logger
def solve_quadratic(a, b, c) -> Optional[Tuple[float, ...]]:
    # Проверяем, что все коэффициенты - числа
    # zip объединяет названия коэффициентов и их значения
    for name, value in zip(("a", "b", "c"), (a, b, c)):
        if not isinstance(value, (int, float)):  # проверяем тип данных
            # Если не число - бросаем исключение TypeError
            raise TypeError(f"Coefficient '{name}' must be numeric")

    # Проверяем особый случай: оба коэффициента a и b равны нулю
    if a == 0 and b == 0:
        # Это критическая ошибка - уравнение не имеет смысла
        raise ValueError("Both coefficients a and b cannot be zero")

    # Проверяем, что a не равно нулю (иначе это не квадратное уравнение)
    if a == 0:
        raise ValueError("a cannot be zero")

    # Вычисляем дискриминант по формуле D = b² - 4ac
    d = b * b - 4 * a * c

    # Если дискриминант отрицательный - действительных корней нет
    if d < 0:
        return None  # возвращаем специальное значение None

    # Если дискриминант равен нулю - один корень
    if d == 0:
        x = -b / (2 * a)  # формула для одного корня
        return (x,)  # возвращаем кортеж с одним элементом

    # Если дискриминант положительный - два корня
    root1 = (-b + math.sqrt(d)) / (2 * a)  # первый корень
    root2 = (-b - math.sqrt(d)) / (2 * a)  # второй корень
    return root1, root2  # возвращаем кортеж с двумя корнями


# Демонстрация работы программы
if __name__ == "__main__":
    print("Демонстрация работы solve_quadratic с логирующим декоратором:")
    print("=" * 60)

    # Тест 1: Уравнение с двумя корнями (уровень INFO)
    print("\n1. INFO - два корня:")
    try:
        # Вызываем функцию для уравнения x² - 3x + 2 = 0
        result = solve_quadratic(1, -3, 2)
        print(f"Результат: {result}")  # Ожидаем (2.0, 1.0)
    except Exception as e:
        print(f"Ошибка: {e}")

    # Тест 2: Дискриминант меньше нуля (уровень WARNING)
    print("\n2. WARNING - дискриминант < 0:")
    try:
        # Вызываем функцию для уравнения x² + 2x + 5 = 0
        result = solve_quadratic(1, 2, 5)
        print(f"Результат: {result}")  # Ожидаем None
    except Exception as e:
        print(f"Ошибка: {e}")

    # Тест 3: Некорректные данные (уровень ERROR)
    print("\n3. ERROR - некорректные данные:")
    try:
        # Пытаемся решить уравнение с текстовым коэффициентом
        result = solve_quadratic("abc", 2, 1)
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")  # Ожидаем TypeError

    # Тест 4: Невозможное уравнение (уровень CRITICAL)
    print("\n4. CRITICAL - невозможная ситуация:")
    try:
        # Пытаемся решить уравнение 0x² + 0x + 5 = 0
        result = solve_quadratic(0, 0, 5)
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")  # Ожидаем ValueError