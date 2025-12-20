import math
import concurrent.futures as ftres
from functools import partial


# Базовая функция для интегрирования
def polynomial_func(x: float) -> float:
    return x ** 2


# 1 итерация: базовая функция
def integrate(f, a: float, b: float, *, n_iter: int = 100000) -> float:
    """
    Вычисляет приближенное значение определенного интеграла функции f от a до b методом прямоугольников

    Аргументы:
    f : callable - функция, которую интегрируем (например, math.sin)
    a : float - начало отрезка интегрирования
    b : float - конец отрезка интегрирования
    n_iter : int, optional - количество прямоугольников

    Возвращает:
    Приближенное значение интеграла

    Пример с тригонометрической функцией:
    >>> round(integrate(math.cos, 0, math.pi/2, n_iter=10000), 3)
    1.0

    Пример с полиномом:
    >>> f = lambda x: x**2
    >>> round(integrate(f, 0, 2, n_iter=10000), 3)
    2.666
    """
    # Начинаем с нуля
    acc = 0

    # Шаг - ширина каждого прямоугольника
    step = (b - a) / n_iter

    # Суммируем площади всех прямоугольников
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


# 2 итерация: функция с потоками
def integrate_threads(f, a: float, b: float, *, n_jobs: int = 2, n_iter: int = 1000) -> float:
    """
       Вычисляет интеграл с использованием многопоточности.

       Аргументы:
       f : callable - интегрируемая функция
       a : float - нижний предел интегрирования
       b : float - верхний предел интегрирования
       n_jobs : int, optional - количество потоков (по умолчанию 2)
       n_iter : int, optional - общее количество прямоугольников (по умолчанию 1000)

       Возвращает:
       Приближенное значение интеграла
       """
    # Создаем пул потоков
    executor = ftres.ThreadPoolExecutor(max_workers=n_jobs)

    # Частично применяем функцию - фиксируем f и n_iter для каждого потока
    spawn = partial(executor.submit, integrate, f, n_iter=n_iter // n_jobs)

    # Делим отрезок на части для каждого потока
    step = (b - a) / n_jobs

    # Каждый поток считает интеграл на своем отрезке
    fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]

    # Ждём результаты и складываем
    return sum(f.result() for f in ftres.as_completed(fs))


# 3 итерация: функция с процессами
def integrate_processes(f, a: float, b: float, *, n_jobs: int = 2, n_iter: int = 1000) -> float:
    """
        Вычисляет интеграл с использованием многопроцессорности.

        Аргументы:
        f : callable - интегрируемая функция
        a : float - нижний предел интегрирования
        b : float - верхний предел интегрирования
        n_jobs : int, optional - количество процессов (по умолчанию 2)
        n_iter : int, optional - общее количество прямоугольников (по умолчанию 1000)

        Возвращает:
        Приближенное значение интеграла
        """
    # Создание отдельных процессов
    executor = ftres.ProcessPoolExecutor(max_workers=n_jobs)

    # Частично применяем функцию - фиксируем f и n_iter для каждого потока
    spawn = partial(executor.submit, integrate, f, n_iter=n_iter // n_jobs)

    # Делим работу между процессами
    step = (b - a) / n_jobs

    # Запускаем процессы
    fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]

    # Собираем результаты
    results = [f.result() for f in ftres.as_completed(fs)]

    # Закрываем пул процессов
    executor.shutdown()

    return sum(results)


# Тесты производительности для разных n_iter
def test_fast():
    # Будем тестировать на sin(x) от 0 до pi
    test_func = math.sin
    a, b = 0, math.pi

    # Разные значения n_iter
    n_iter_list = [1000, 5000, 10000, 50000]

    for n in n_iter_list:
        import time

        # Замеряем время
        start = time.time()
        result = integrate(test_func, a, b, n_iter=n)
        end = time.time()

        print(f"n_iter = {n:8d}: время = {end - start:.6f} сек, результат = {result:.8f}")


# Сравнение потоков и процессов
def compare_threads_processes():
    # Теоретический результат: ∫x²dx от 0 до 2 = 8/3 ≈ 2.666667
    theoretical = 8 / 3

    print(f"Теоретическое значение: {theoretical:.6f}")

    # Количество ядер для теста
    n_jobs_list = [2, 4, 6, 8]

    for n_jobs in n_jobs_list:
        import time

        # Тестируем потоки
        start = time.time()
        result_thread = integrate_threads(polynomial_func, 0, 2, n_jobs=n_jobs, n_iter=500000)
        time_thread = time.time() - start

        # Тестируем процессы
        start = time.time()
        result_process = integrate_processes(polynomial_func, 0, 2, n_jobs=n_jobs, n_iter=500000)
        time_process = time.time() - start

        print(f"\nn_jobs = {n_jobs}:")
        print(f"  Потоки: {time_thread:.4f} сек, результат: {result_thread:.6f}")
        print(f"  Процессы: {time_process:.4f} сек, результат: {result_process:.6f}")


def main():
    import doctest

    # Запускаем тесты из docstring
    doctest.testmod(verbose=False)

    # Тест 1: cos(x) от 0 до pi/2
    result1 = integrate(math.cos, 0, math.pi / 2, n_iter=10000)
    print(f"∫cos(x)dx от 0 до π/2 = {result1:.6f} (должно быть ~1.0)")

    # Тест 2: x^2 от 0 до 2
    result2 = integrate(lambda x: x ** 2, 0, 2, n_iter=10000)
    print(f"∫x²dx от 0 до 2 = {result2:.6f} (должно быть ~2.666667)")

    # Тесты производительности
    test_fast()

    # Сравнение потоков и процессов
    compare_threads_processes()

    # Проверяем doctest


if __name__ == "__main__":
    main()
