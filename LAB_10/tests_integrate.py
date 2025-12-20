import unittest
import math

# Импортируем функции
from integrates_func_1_3 import integrate, integrate_threads, integrate_processes, polynomial_func


class TestIntegrate(unittest.TestCase):

    def test_cos_integral(self):
        """Тест интеграла cos(x) от 0 до pi/2"""
        # Теоретическое значение: 1.0
        result = integrate(math.cos, 0, math.pi / 2, n_iter=10000)
        # Проверяем с точностью до 0.001
        self.assertAlmostEqual(result, 1.0, places=3)

    def test_poly_integral(self):
        """Тест интеграла x^2 от 0 до 2"""
        f = lambda x: x ** 2
        # Теоретическое значение: 8/3 ≈ 2.666667
        result = integrate(f, 0, 2, n_iter=10000)
        self.assertAlmostEqual(result, 8 / 3, places=3)

    def test_more_accurate(self):
        """Проверка, что больше итераций = точнее"""
        f = lambda x: x ** 3

        # Считаем с разным количеством итераций
        result1 = integrate(f, 0, 1, n_iter=100)
        result2 = integrate(f, 0, 1, n_iter=1000)
        result3 = integrate(f, 0, 1, n_iter=10000)

        # Теоретическое значение: 0.25
        theoretical = 0.25

        # Ошибка должна уменьшаться
        error1 = abs(result1 - theoretical)
        error2 = abs(result2 - theoretical)
        error3 = abs(result3 - theoretical)

        # Проверяем, что ошибка уменьшается
        self.assertLess(error2, error1)
        self.assertLess(error3, error2)

    def test_async_correctness(self):
        """Проверка, что многопоточная версия работает правильно"""
        result_async = integrate_threads(math.sin, 0, math.pi, n_jobs=2, n_iter=10000)
        result_sync = integrate(math.sin, 0, math.pi, n_iter=10000)

        self.assertAlmostEqual(result_async, result_sync, places=4)

    def test_processes_correctness(self):
        """Проверка, что многопроцессорная версия работает правильно"""
        result_process = integrate_processes(polynomial_func, 0, 2, n_jobs=2, n_iter=10000)
        result_sync = integrate(polynomial_func, 0, 2, n_iter=10000)

        self.assertAlmostEqual(result_process, result_sync, places=4)


def run_tests():
    """Запускаем все тесты"""
    # Создаем TestSuite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIntegrate)

    # Запускаем
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return result


if __name__ == '__main__':
    result = run_tests()
