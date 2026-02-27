# 
# Лабораторная работа: Численные вычисления и анализ данных с использованием NumPy

# Формат выполнения: самостоятельная работа.

# Перед началом:
# 1. Создайте виртуальное окружение:
#    python -m venv numpy_env
   
# 2. Активируйте виртуальное окружение:
#    - Windows: numpy_env\Scripts\activate
#    - Linux/Mac: source numpy_env/bin/activate
   
# 3. Установите зависимости:
#    pip install numpy matplotlib seaborn pandas pytest

# Структура проекта:

# numpy_lab/
# ├── main.py
# ├── test.py
# ├── data/
# │   └── students_scores.csv
# └── plots/

# В папке data создайте файл students_scores.csv со следующим содержимым:

# math,physics,informatics
# 78,81,90
# 85,89,88
# 92,94,95
# 70,75,72
# 88,84,91
# 95,99,98
# 60,65,70
# 73,70,68
# 84,86,85
# 90,93,92

# (Дополнительно можно использовать публичные датасеты Kaggle:
# Students Performance Dataset:
# https://www.kaggle.com/datasets/spscientist/students-performance-in-exams
# или любой аналогичный табличный CSV)

# Задача: реализовать все функции, чтобы проходили тесты.
# 

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 1. СОЗДАНИЕ И ОБРАБОТКА МАССИВОВ
# ============================================================

def create_vector():
    """
    Создать массив от 0 до 9.

    Изучить:
    https://numpy.org/doc/stable/reference/generated/numpy.arange.html
    
    Returns:
        numpy.ndarray: Массив чисел от 0 до 9 включительно
    """
    # Подсказка: используйте np.arange(10)
    pass


def create_matrix():
    """
    Создать матрицу 5x5 со случайными числами [0,1].

    Изучить:
    https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html
    
    Returns:
        numpy.ndarray: Матрица 5x5 со случайными значениями от 0 до 1
    """
    # Подсказка: используйте np.random.rand(5,5)
    pass


def reshape_vector(vec):
    """
    Преобразовать (10,) -> (2,5)

    Изучить:
    https://numpy.org/doc/stable/reference/generated/numpy.reshape.html
    
    Args:
        vec (numpy.ndarray): Входной массив формы (10,)
    
    Returns:
        numpy.ndarray: Преобразованный массив формы (2, 5)
    """
    # Подсказка: используйте vec.reshape(2,5)
    pass


def transpose_matrix(mat):
    """
    Транспонирование матрицы.

    Изучить:
    https://numpy.org/doc/stable/reference/generated/numpy.transpose.html
    
    Args:
        mat (numpy.ndarray): Входная матрица
    
    Returns:
        numpy.ndarray: Транспонированная матрица
    """
    # Подсказка: используйте mat.T или np.transpose(mat)
    pass


# ============================================================
# 2. ВЕКТОРНЫЕ ОПЕРАЦИИ
# ============================================================

def vector_add(a, b):
    """
    Сложение векторов одинаковой длины.
    (Векторизация без циклов)
    
    Args:
        a (numpy.ndarray): Первый вектор
        b (numpy.ndarray): Второй вектор
    
    Returns:
        numpy.ndarray: Результат поэлементного сложения
    """
    # Подсказка: используйте оператор +
    pass


def scalar_multiply(vec, scalar):
    """
    Умножение вектора на число.
    
    Args:
        vec (numpy.ndarray): Входной вектор
        scalar (float/int): Число для умножения
    
    Returns:
        numpy.ndarray: Результат умножения вектора на скаляр
    """
    # Подсказка: используйте оператор *
    pass


def elementwise_multiply(a, b):
    """
    Поэлементное умножение.
    
    Args:
        a (numpy.ndarray): Первый вектор/матрица
        b (numpy.ndarray): Второй вектор/матрица
    
    Returns:
        numpy.ndarray: Результат поэлементного умножения
    """
    # Подсказка: используйте оператор *
    pass


def dot_product(a, b):
    """
    Скалярное произведение.

    Изучить:
    https://numpy.org/doc/stable/reference/generated/numpy.dot.html
    
    Args:
        a (numpy.ndarray): Первый вектор
        b (numpy.ndarray): Второй вектор
    
    Returns:
        float: Скалярное произведение векторов
    """
    # Подсказка: используйте np.dot(a, b)
    pass


# ============================================================
# 3. МАТРИЧНЫЕ ОПЕРАЦИИ
# ============================================================

def matrix_multiply(a, b):
    """
    Умножение матриц.

    Изучить:
    https://numpy.org/doc/stable/reference/generated/numpy.matmul.html
    
    Args:
        a (numpy.ndarray): Первая матрица
        b (numpy.ndarray): Вторая матрица
    
    Returns:
        numpy.ndarray: Результат умножения матриц
    """
    # Подсказка: используйте a @ b или np.matmul(a, b)
    pass


def matrix_determinant(a):
    """
    Определитель матрицы.

    Изучить:
    https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html
    
    Args:
        a (numpy.ndarray): Квадратная матрица
    
    Returns:
        float: Определитель матрицы
    """
    # Подсказка: используйте np.linalg.det(a)
    pass


def matrix_inverse(a):
    """
    Обратная матрица.

    Изучить:
    https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html
    
    Args:
        a (numpy.ndarray): Квадратная матрица
    
    Returns:
        numpy.ndarray: Обратная матрица
    """
    # Подсказка: используйте np.linalg.inv(a)
    pass


def solve_linear_system(a, b):
    """
    Решить систему Ax = b

    Изучить:
    https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html
    
    Args:
        a (numpy.ndarray): Матрица коэффициентов A
        b (numpy.ndarray): Вектор свободных членов b
    
    Returns:
        numpy.ndarray: Решение системы x
    """
    # Подсказка: используйте np.linalg.solve(a, b)
    pass


# ============================================================
# 4. СТАТИСТИЧЕСКИЙ АНАЛИЗ
# ============================================================

def load_dataset(path="data/students_scores.csv"):
    """
    Загрузить CSV и вернуть NumPy массив.
    
    Args:
        path (str): Путь к CSV файлу
    
    Returns:
        numpy.ndarray: Загруженные данные в виде массива
    """
    # Подсказка: используйте pd.read_csv(path).to_numpy()
    pass


def statistical_analysis(data):
    """
    Представьте, что данные — это результаты экзамена по математике.
    Нужно оценить:
    - средний балл
    - медиану
    - стандартное отклонение
    - минимум
    - максимум
    - 25 и 75 перцентили

    Изучить:
    https://numpy.org/doc/stable/reference/generated/numpy.mean.html
    https://numpy.org/doc/stable/reference/generated/numpy.median.html
    https://numpy.org/doc/stable/reference/generated/numpy.std.html
    https://numpy.org/doc/stable/reference/generated/numpy.percentile.html
    
    Args:
        data (numpy.ndarray): Одномерный массив данных
    
    Returns:
        dict: Словарь со статистическими показателями
    """
    # Подсказка: используйте np.mean(), np.median(), np.std(), 
    # np.min(), np.max(), np.percentile(data, 25), np.percentile(data, 75)
    pass


def normalize_data(data):
    """
    Min-Max нормализация.
    
    Формула: (x - min) / (max - min)
    
    Args:
        data (numpy.ndarray): Входной массив данных
    
    Returns:
        numpy.ndarray: Нормализованный массив данных в диапазоне [0, 1]
    """
    # Подсказка: вычислите min и max с помощью np.min() и np.max()
    pass


# ============================================================
# 5. ВИЗУАЛИЗАЦИЯ
# ============================================================

def plot_histogram(data):
    """
    Построить гистограмму распределения оценок по математике.

    Изучить:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
    
    Args:
        data (numpy.ndarray): Данные для гистограммы
    """
    # Подсказка: используйте plt.hist(), добавьте заголовок, подписи осей,
    # сохраните в папку plots с помощью plt.savefig()
    pass


def plot_heatmap(matrix):
    """
    Построить тепловую карту корреляции предметов.

    Изучить:
    https://seaborn.pydata.org/generated/seaborn.heatmap.html
    
    Args:
        matrix (numpy.ndarray): Матрица корреляции
    """
    # Подсказка: используйте sns.heatmap(), добавьте заголовок, сохраните
    pass


def plot_line(x, y):
    """
    Построить график зависимости: студент -> оценка по математике.

    Изучить:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
    
    Args:
        x (numpy.ndarray): Номера студентов
        y (numpy.ndarray): Оценки студентов
    """
    # Подсказка: используйте plt.plot(), добавьте заголовок, подписи осей,
    # сохраните график
    pass


# ============================================================
# ========================== ТЕСТЫ ===========================
# ============================================================

def test_create_vector():
    v = create_vector()
    assert isinstance(v, np.ndarray)
    assert v.shape == (10,)
    assert np.array_equal(v, np.arange(10))


def test_create_matrix():
    m = create_matrix()
    assert isinstance(m, np.ndarray)
    assert m.shape == (5, 5)
    assert np.all((m >= 0) & (m < 1))


def test_reshape_vector():
    v = np.arange(10)
    reshaped = reshape_vector(v)
    assert reshaped.shape == (2, 5)
    assert reshaped[0, 0] == 0
    assert reshaped[1, 4] == 9


def test_vector_add():
    assert np.array_equal(
        vector_add(np.array([1,2,3]), np.array([4,5,6])),
        np.array([5,7,9])
    )
    assert np.array_equal(
        vector_add(np.array([0,1]), np.array([1,1])),
        np.array([1,2])
    )


def test_scalar_multiply():
    assert np.array_equal(
        scalar_multiply(np.array([1,2,3]), 2),
        np.array([2,4,6])
    )


def test_elementwise_multiply():
    assert np.array_equal(
        elementwise_multiply(np.array([1,2,3]), np.array([4,5,6])),
        np.array([4,10,18])
    )


def test_dot_product():
    assert dot_product(np.array([1,2,3]), np.array([4,5,6])) == 32
    assert dot_product(np.array([2,0]), np.array([3,5])) == 6


def test_matrix_multiply():
    A = np.array([[1,2],[3,4]])
    B = np.array([[2,0],[1,2]])
    assert np.array_equal(matrix_multiply(A,B), A @ B)


def test_matrix_determinant():
    A = np.array([[1,2],[3,4]])
    assert round(matrix_determinant(A),5) == -2.0


def test_matrix_inverse():
    A = np.array([[1,2],[3,4]])
    invA = matrix_inverse(A)
    assert np.allclose(A @ invA, np.eye(2))


def test_solve_linear_system():
    A = np.array([[2,1],[1,3]])
    b = np.array([1,2])
    x = solve_linear_system(A,b)
    assert np.allclose(A @ x, b)


def test_load_dataset():
    # Для теста создадим временный файл
    test_data = "math,physics,informatics\n78,81,90\n85,89,88"
    with open("test_data.csv", "w") as f:
        f.write(test_data)
    try:
        data = load_dataset("test_data.csv")
        assert data.shape == (2, 3)
        assert np.array_equal(data[0], [78,81,90])
    finally:
        os.remove("test_data.csv")


def test_statistical_analysis():
    data = np.array([10,20,30])
    result = statistical_analysis(data)
    assert result["mean"] == 20
    assert result["min"] == 10
    assert result["max"] == 30


def test_normalization():
    data = np.array([0,5,10])
    norm = normalize_data(data)
    assert np.allclose(norm, np.array([0,0.5,1]))


def test_plot_histogram():
    # Просто проверяем, что функция не падает
    data = np.array([1,2,3,4,5])
    plot_histogram(data)


def test_plot_heatmap():
    matrix = np.array([[1,0.5],[0.5,1]])
    plot_heatmap(matrix)


def test_plot_line():
    x = np.array([1,2,3])
    y = np.array([4,5,6])
    plot_line(x, y)


if __name__ == "__main__":
    print("Запустите python3 -m pytest test.py -v для проверки лабораторной работы.")
