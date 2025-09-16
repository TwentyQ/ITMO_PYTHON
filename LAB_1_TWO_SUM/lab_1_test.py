import unittest # Импорт встроенного модуля для unit-тестирования
import two_sum # Импорт модуля для тестирования

# Тесты
class TestTwoSumma(unittest.TestCase):

    # Тест с положительными числами
    def test_summa_positive(self):
        self.assertEqual(two_sum.two_summa([2, 7, 11, 15], 9), [0, 1])

    # Тест с отрицательными числами
    def test_summa_negative(self):
        self.assertEqual(two_sum.two_summa([-1, -2, -4, -2], -4), [1, 3])

    # Тест массива, который не имеет значений
    def test_summa_zero(self):
        self.assertEqual(two_sum.two_summa([2, 5, 4, 5, 6], 23), [])

    # Тест с нулями в массиве и в переменной target
    def test_summa_zero_in_massive(self):
        self.assertEqual(two_sum.two_summa([0, 5, 0, 8, 4], 0), [0, 2])

    # Тест с большими числами
    def test_summa_large_numbers(self):
        self.assertEqual(two_sum.two_summa([254300, 5333333, 4000000, 522323, 66666], 588989), [3, 4])

    # Тест с одинаковыми суммами разных пар индексов
    def test_summa_sameness(self):
        self.assertEqual(two_sum.two_summa([6, 7, 6, 7], 13), [0, 1])

    # Тест с повторяющимися одинаковыми числами в массиве
    def test_summa_one_number(self):
        self.assertEqual(two_sum.two_summa([5, 5, 5, 5], 10), [0, 1])


# Запуск тестов
if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
