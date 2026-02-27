import numpy as np
import os
from main import (
    create_vector, create_matrix, reshape_vector, transpose_matrix,
    vector_add, scalar_multiply, elementwise_multiply, dot_product,
    matrix_multiply, matrix_determinant, matrix_inverse, solve_linear_system,
    load_dataset, statistical_analysis, normalize_data,
    plot_histogram, plot_heatmap, plot_line
)


# ============================================================
# ========================== ТЕСТЫ ===========================
# ============================================================

def test_create_vector() -> None:
    """
    Тест создания вектора от 0 до 9.
    """
    v = create_vector()
    assert isinstance(v, np.ndarray)
    assert v.shape == (10,)
    assert np.array_equal(v, np.arange(10))


def test_create_matrix() -> None:
    """
    Тест создания матрицы 5x5 со случайными числами.
    """
    m: np.ndarray = create_matrix()
    assert isinstance(m, np.ndarray)
    assert m.shape == (5, 5)
    assert np.all((m >= 0) & (m < 1))


def test_reshape_vector() -> None:
    """
    Тест преобразования вектора из формы (10,) в (2, 5).
    """
    v: np.ndarray = np.arange(10)
    reshaped = reshape_vector(v)
    assert reshaped.shape == (2, 5)
    assert reshaped[0, 0] == 0
    assert reshaped[1, 4] == 9


def test_vector_add() -> None:
    """
    Тест сложения векторов.
    """
    assert np.array_equal(
        vector_add(np.array([1, 2, 3]), np.array([4, 5, 6])),
        np.array([5, 7, 9])
    )
    assert np.array_equal(
        vector_add(np.array([0, 1]), np.array([1, 1])),
        np.array([1, 2])
    )


def test_scalar_multiply() -> None:
    """
    Тест умножения вектора на скаляр.
    """
    assert np.array_equal(
        scalar_multiply(np.array([1, 2, 3]), 2),
        np.array([2, 4, 6])
    )


def test_elementwise_multiply() -> None:
    """
    Тест поэлементного умножения векторов.
    """
    assert np.array_equal(
        elementwise_multiply(np.array([1, 2, 3]), np.array([4, 5, 6])),
        np.array([4, 10, 18])
    )


def test_dot_product() -> None:
    """
    Тест скалярного произведения векторов.
    """
    assert dot_product(np.array([1, 2, 3]), np.array([4, 5, 6])) == 32
    assert dot_product(np.array([2, 0]), np.array([3, 5])) == 6


def test_matrix_multiply() -> None:
    """
    Тест умножения матриц.
    """
    A: np.ndarray = np.array([[1, 2], [3, 4]])
    B: np.ndarray = np.array([[2, 0], [1, 2]])
    assert np.array_equal(matrix_multiply(A, B), A @ B)


def test_matrix_determinant() -> None:
    """
    Тест вычисления определителя матрицы.
    """
    A: np.ndarray = np.array([[1, 2], [3, 4]])
    assert round(matrix_determinant(A), 5) == -2.0


def test_matrix_inverse() -> None:
    """
    Тест вычисления обратной матрицы.
    """
    A: np.ndarray = np.array([[1, 2], [3, 4]])
    invA: np.ndarray = matrix_inverse(A)
    assert np.allclose(A @ invA, np.eye(2))


def test_solve_linear_system() -> None:
    """
    Тест решения системы линейных уравнений.
    """
    A: np.ndarray = np.array([[2, 1], [1, 3]])
    b: np.ndarray = np.array([1, 2])
    x: np.ndarray = solve_linear_system(A, b)
    assert np.allclose(A @ x, b)


def test_load_dataset() -> None:
    """
    Тест загрузки данных из CSV файла.
    """
    # Для теста создадим временный файл
    test_data: str = "math,physics,informatics\n78,81,90\n85,89,88"
    with open("test_data.csv", "w") as f:
        f.write(test_data)
    try:
        data: np.ndarray = load_dataset("test_data.csv")
        assert data.shape == (2, 3)
        assert np.array_equal(data[0], [78, 81, 90])
    finally:
        os.remove("test_data.csv")


def test_statistical_analysis() -> None:
    """
    Тест статистического анализа данных.
    """
    data: np.ndarray = np.array([10, 20, 30])
    result: dict[str, float] = statistical_analysis(data)
    assert result["mean"] == 20
    assert result["min"] == 10
    assert result["max"] == 30
    assert result["25_percentile"] == 15
    assert result["75_percentile"] == 25


def test_normalization() -> None:
    """
    Тест Min-Max нормализации данных.
    """
    data: np.ndarray = np.array([0, 5, 10])
    norm: np.ndarray = normalize_data(data)
    assert np.allclose(norm, np.array([0, 0.5, 1]))


def test_plot_histogram() -> None:
    """
    Тест построения гистограммы.
    """
    data: np.ndarray = np.array([1, 2, 3, 4, 5])
    plot_histogram(data)


def test_plot_heatmap() -> None:
    """
    Тест построения тепловой карты.
    """
    matrix: np.ndarray = np.array([[1, 0.5], [0.5, 1]])
    plot_heatmap(matrix)


def test_plot_line() -> None:
    """
    Тест построения линейного графика.
    """
    x: np.ndarray = np.array([1, 2, 3])
    y: np.ndarray = np.array([4, 5, 6])
    plot_line(x, y)
