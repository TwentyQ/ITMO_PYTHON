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

# Задача: реализовать все функции, чтобы проходили тесты.

import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns

matplotlib.use('Agg')
import matplotlib.pyplot as plt


# ============================================================
# 1. СОЗДАНИЕ И ОБРАБОТКА МАССИВОВ
# ============================================================

def create_vector() -> np.ndarray:
    """
    Создать массив от 0 до 9.
    
    Returns:
        numpy.ndarray: Массив чисел от 0 до 9 включительно
    """
    return np.arange(0, 10)


def create_matrix() -> np.ndarray:
    """
    Создать матрицу 5x5 со случайными числами [0,1].

    Returns:
        numpy.ndarray: Матрица 5x5 со случайными значениями от 0 до 1
    """
    return (np.random.rand(5, 5))


def reshape_vector(vec: np.ndarray) -> np.ndarray:
    """
    Преобразование (10,) -> (2,5)
    
    Args:
        vec (numpy.ndarray): Входной массив формы (10,)
    
    Returns:
        numpy.ndarray: Преобразованный массив формы (2, 5)
    """
    return (np.reshape(vec, (2, 5)))


def transpose_matrix(mat: np.ndarray) -> np.ndarray:
    """
    Транспонирование матрицы.

    Args:
        mat (numpy.ndarray): Входная матрица
    
    Returns:
        numpy.ndarray: Транспонированная матрица
    """
    return np.transpose(mat)


# ============================================================
# 2. ВЕКТОРНЫЕ ОПЕРАЦИИ
# ============================================================

def vector_add(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Сложение векторов одинаковой длины.
    (Векторизация без циклов)
    
    Args:
        a (numpy.ndarray): Первый вектор
        b (numpy.ndarray): Второй вектор
    
    Returns:
        numpy.ndarray: Результат поэлементного сложения
    """
    return a + b


def scalar_multiply(vec: np.ndarray, scalar: float | int) -> np.ndarray:
    """
    Умножение вектора на число.
    
    Args:
        vec (numpy.ndarray): Входной вектор
        scalar (float/int): Число для умножения
    
    Returns:
        numpy.ndarray: Результат умножения вектора на скаляр
    """
    return vec * scalar


def elementwise_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Поэлементное умножение.
    
    Args:
        a (numpy.ndarray): Первый вектор/матрица
        b (numpy.ndarray): Второй вектор/матрица
    
    Returns:
        numpy.ndarray: Результат поэлементного умножения
    """
    return a * b


def dot_product(a: np.ndarray, b: np.ndarray) -> float:
    """
    Скалярное произведение.
    
    Args:
        a (numpy.ndarray): Первый вектор
        b (numpy.ndarray): Второй вектор
    
    Returns:
        float: Скалярное произведение векторов
    """
    return (np.dot(a, b))


# ============================================================
# 3. МАТРИЧНЫЕ ОПЕРАЦИИ
# ============================================================

def matrix_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Умножение матриц.

    Args:
        a (numpy.ndarray): Первая матрица
        b (numpy.ndarray): Вторая матрица
    
    Returns:
        numpy.ndarray: Результат умножения матриц
    """
    return np.matmul(a, b)


def matrix_determinant(a: np.ndarray) -> float:
    """
    Определитель матрицы.

    Args:
        a (numpy.ndarray): Квадратная матрица
    
    Returns:
        float: Определитель матрицы
    """
    return (np.linalg.det(a))


def matrix_inverse(a: np.ndarray) -> np.ndarray:
    """
    Обратная матрица.

    Args:
        a (numpy.ndarray): Квадратная матрица
    
    Returns:
        numpy.ndarray: Обратная матрица
    """
    return (np.linalg.inv(a))


def solve_linear_system(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Решить систему Ax = b

    Args:
        a (numpy.ndarray): Матрица коэффициентов A
        b (numpy.ndarray): Вектор свободных членов b
    
    Returns:
        numpy.ndarray: Решение системы x
    """
    return (np.linalg.solve(a, b))


# ============================================================
# 4. СТАТИСТИЧЕСКИЙ АНАЛИЗ
# ============================================================

def load_dataset(path: str = "data/students_scores.csv") -> np.ndarray:
    """
    Загрузить CSV и вернуть NumPy массив.
    
    Args:
        path (str): Путь к CSV файлу
    
    Returns:
        numpy.ndarray: Загруженные данные в виде массива
    """
    return (pd.read_csv(path).to_numpy())


def statistical_analysis(data: np.ndarray) -> dict[str, float]:
    """
    Представьте, что данные — это результаты экзамена по математике.
    Нужно оценить:
    - средний балл
    - медиану
    - стандартное отклонение
    - минимум
    - максимум
    - 25 и 75 перцентили

    Args:
        data (numpy.ndarray): Одномерный массив данных
    
    Returns:
        dict: Словарь со статистическими показателями
    """
    stats = {
        "mean": np.mean(data),
        "median": np.median(data),
        "std": np.std(data),
        "min": np.min(data),
        "max": np.max(data),
        "25_percentile": np.percentile(data, 25),
        "75_percentile": np.percentile(data, 75)
    }
    return stats


def normalize_data(data: np.ndarray) -> np.ndarray:
    """
    Min-Max нормализация.

    Формула: (x - min) / (max - min)

    Args:
        data (numpy.ndarray): Входной массив данных

    Returns:
        numpy.ndarray: Нормализованный массив данных в диапазоне [0, 1]
    """
    data_min: float = float(np.min(data))
    data_max: float = float(np.max(data))

    if data_max - data_min == 0:
        return np.zeros_like(data)

    return (data - data_min) / (data_max - data_min)


# ============================================================
# 5. ВИЗУАЛИЗАЦИЯ
# ============================================================

def plot_histogram(data: np.ndarray) -> None:
    """
    Построить гистограмму распределения оценок по математике.

    Args:
        data (numpy.ndarray): Данные для гистограммы
    """
    # Подсказка: используйте plt.hist(), добавьте заголовок, подписи осей,
    # сохраните в папку plots с помощью plt.savefig()
    plt.hist(data)
    plt.xlabel('Оценка')
    plt.ylabel('Частота')
    plt.savefig('plots/histogram.png')
    plt.close()


def plot_heatmap(matrix: np.ndarray) -> None:
    """
    Построить тепловую карту корреляции предметов.
    
    Args:
        matrix (numpy.ndarray): Матрица корреляции
    """
    # Подсказка: используйте sns.heatmap(), добавьте заголовок, сохраните
    sns.heatmap(matrix, annot=True, xticklabels=['Математика', 'Физика', 'Информатика'],
                yticklabels=['Математика', 'Физика', 'Информатика'])
    plt.title('Матрица корреляции предметов')
    plt.savefig('plots/heatmap.png')
    plt.close()


def plot_line(x: np.ndarray, y: np.ndarray) -> None:
    """
    Построить график зависимости: студент -> оценка по математике.

    Args:
        x (numpy.ndarray): Номера студентов
        y (numpy.ndarray): Оценки студентов
    """
    plt.plot(x, y)
    plt.title('Оценки студентов по математике')
    plt.xlabel('Номер студента')
    plt.ylabel('Оценка')
    plt.savefig('plots/line_plot.png')
    plt.close()


if __name__ == "__main__":
    print("Запустите python -m pytest test.py -v для проверки лабораторной работы.")
