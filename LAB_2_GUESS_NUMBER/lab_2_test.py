import unittest  # Импорт встроенного модуля для unit-тестирования
import guess_number # Импорт пользовательского модуля для тестирования



# Тесты
class TestGuessNumber(unittest.TestCase):
    # Тесты с последовательным алгоритмом поиска

    '''Тест: число найдено - обычный список'''

    def test_found_number_seq(self):
        self.assertEqual(guess_number.guess_number(6, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'seq'), [6, 6])

    '''Тест: число не найдено - обычный список'''

    def test_not_found_number_seq(self):
        self.assertEqual(guess_number.guess_number(11, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'seq'), [11, None])

    '''Тест: список с различными числами'''

    def test_random_number_seq(self):
        self.assertEqual(guess_number.guess_number(66, [56, 25, 3, 43, 5, 6, 66, 82, -9, 10000], 'seq'), [66, 8])

    '''Тест: отрицательные числа'''

    def test_found_negative_number_seq(self):
        self.assertEqual(guess_number.guess_number(-6, [1, -2, 3, 4, 5, -6, 7, 8, 9, -10], 'seq'), [-6, 2])

    ''' Тест: искомое число повторяется в списке многократно'''

    def test_found_same_number_seq(self):
        self.assertEqual(guess_number.guess_number(6, [1, 2, 3, 4, 5, 6, 7, 8, 6, 6], 'seq'), [6, 6])

    '''Тест: пустой список'''

    def test_empty_list_seq(self):
        self.assertEqual(guess_number.guess_number(6, [], 'seq'), [6, None])

    # Тесты с последовательным алгоритмом поиска

    '''Тест: число найдено - обычный список'''

    def test_found_number_bin(self):
        self.assertEqual(guess_number.guess_number(6, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'bin'), [6, 3])

    '''Тест: число не найдено - обычный список'''

    def test_not_found_number_bin(self):
        self.assertEqual(guess_number.guess_number(11, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'bin'), [11, None])

    '''Тест: список с различными числами'''

    def test_random_number_bin(self):
        self.assertEqual(guess_number.guess_number(66, [56, 25, 3, 43, 5, 66, 756, 82, -9, 10000], 'bin'), [66, 4])

    '''Тест: отрицательные числа'''

    def test_found_negative_number_bin(self):
        self.assertEqual(guess_number.guess_number(-6, [1, -2, 3, 4, 5, -6, 7, 8, 9, -10], 'bin'), [-6, 2])

    '''Тест: искомое число повторяется в списке многократно'''

    def test_found_same_number_bin(self):
        self.assertEqual(guess_number.guess_number(6, [1, 2, 3, 4, 5, 6, 7, 8, 6, 6], 'bin'), [6, 2])

    '''Тест: пустой список'''

    def test_empty_list_bin(self):
        self.assertEqual(guess_number.guess_number(6, [], 'bin'), [6, None])


# Запуск тестов
if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)

