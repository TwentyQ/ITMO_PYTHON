# Директивы для оптимизации
# cython: language_level=3 # Указываем Cython использовать Python 3 синтаксис
# cython: boundscheck=False # Отключаем проверку границ массивов для скорости
# cython: wraparound=False # Отключаем циклический доступ к массивам для скорости

from libc.math cimport sin, cos # Импортируем C функции из math
cimport cython  # Импортируем Cython
from cython.parallel cimport prange, parallel # Импортируем функции параллельного выполнения

def integrate_cython(f, double a, double b, int n_iter=100000):
    """Cython версия функции integrate"""
    cdef double acc = 0.0 # Объявляем переменную acc как double для накопления суммы
    cdef double step = (b - a) / n_iter # Вычисляем шаг интегрирования
    cdef double x # Объявляем переменную x для текущей точки
    cdef int i # Объявляем переменную i как целое число для цикла

    for i in range(n_iter): # Цикл по всем итерациям интегрирования
        x = a + i * step # Вычисляем текущую точку x
        acc += f(x) * step # Добавляем площадь текущего прямоугольника к сумме

    return acc


# Простая noGIL версия для синуса
def integrate_sin_nogil(double a, double b, int n_jobs=2, int n_iter=100000):
    """noGIL версия для sin(x)"""
    cdef double step = (b - a) / n_jobs # Вычисляем размер шага для каждого потока
    cdef double total = 0.0 # Объявляем переменную для общего результата
    cdef int i # Объявляем счетчики циклов
    cdef int chunk_iter = n_iter // n_jobs # Вычисляем количество итераций на каждый поток
    cdef double acc # Объявляем переменную для накопления в каждом потоке
    cdef double chunk_a, chunk_b, chunk_step # Объявляем переменные для границ каждого отрезка
    cdef int j # Объявляем счетчик для внутреннего цикла
    cdef double x # Объявляем переменную для текущей точки

    # Внешний цикл по количеству потоков
    for i in range(n_jobs):
        acc = 0.0
        chunk_a = a + i * step
        chunk_b = a + (i + 1) * step
        chunk_step = (chunk_b - chunk_a) / chunk_iter

        # Внутренний цикл по итерациям в текущем отрезке
        for j in range(chunk_iter):
            x = chunk_a + j * chunk_step
            acc += sin(x) * chunk_step

        total += acc

    return total # Возвращаем общий результат интегрирования
