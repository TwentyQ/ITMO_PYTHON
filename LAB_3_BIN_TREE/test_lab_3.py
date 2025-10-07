import unittest
import gen_tree  # Теперь импорт сработает


class TestTree(unittest.TestCase):
    """Тесты для функции gen_bin_tree (вариант 5)"""

    def test_var_5(self):
        """Тест: вариант 5(Root = 5
        height = 6, left_leaf = root^2, right_leaf = root-2)"""
        result = gen_tree.gen_bin_tree(height = 6, root = 5)
        expected = {'root': 5, 'left': {'root': 25, 'left': {'root': 625, 'left': {'root': 390625, 'left': {'root': 152587890625, 'left': {'root': 23283064365386962890625, 'left': None, 'right': None}, 'right': {'root': 152587890623, 'left': None, 'right': None}}, 'right': {'root': 390623, 'left': {'root': 152586328129, 'left': None, 'right': None}, 'right': {'root': 390621, 'left': None, 'right': None}}}, 'right': {'root': 623, 'left': {'root': 388129, 'left': {'root': 150644120641, 'left': None, 'right': None}, 'right': {'root': 388127, 'left': None, 'right': None}}, 'right': {'root': 621, 'left': {'root': 385641, 'left': None, 'right': None}, 'right': {'root': 619, 'left': None, 'right': None}}}}, 'right': {'root': 23, 'left': {'root': 529, 'left': {'root': 279841, 'left': {'root': 78310985281, 'left': None, 'right': None}, 'right': {'root': 279839, 'left': None, 'right': None}}, 'right': {'root': 527, 'left': {'root': 277729, 'left': None, 'right': None}, 'right': {'root': 525, 'left': None, 'right': None}}}, 'right': {'root': 21, 'left': {'root': 441, 'left': {'root': 194481, 'left': None, 'right': None}, 'right': {'root': 439, 'left': None, 'right': None}}, 'right': {'root': 19, 'left': {'root': 361, 'left': None, 'right': None}, 'right': {'root': 17, 'left': None, 'right': None}}}}}, 'right': {'root': 3, 'left': {'root': 9, 'left': {'root': 81, 'left': {'root': 6561, 'left': {'root': 43046721, 'left': None, 'right': None}, 'right': {'root': 6559, 'left': None, 'right': None}}, 'right': {'root': 79, 'left': {'root': 6241, 'left': None, 'right': None}, 'right': {'root': 77, 'left': None, 'right': None}}}, 'right': {'root': 7, 'left': {'root': 49, 'left': {'root': 2401, 'left': None, 'right': None}, 'right': {'root': 47, 'left': None, 'right': None}}, 'right': {'root': 5, 'left': {'root': 25, 'left': None, 'right': None}, 'right': {'root': 3, 'left': None, 'right': None}}}}, 'right': {'root': 1, 'left': {'root': 1, 'left': {'root': 1, 'left': {'root': 1, 'left': None, 'right': None}, 'right': {'root': -1, 'left': None, 'right': None}}, 'right': {'root': -1, 'left': {'root': 1, 'left': None, 'right': None}, 'right': {'root': -3, 'left': None, 'right': None}}}, 'right': {'root': -1, 'left': {'root': 1, 'left': {'root': 1, 'left': None, 'right': None}, 'right': {'root': -1, 'left': None, 'right': None}}, 'right': {'root': -3, 'left': {'root': 9, 'left': None, 'right': None}, 'right': {'root': -5, 'left': None, 'right': None}}}}}}
        self.assertEqual(result, expected)

    def test_height_1(self):
        """Тест: дерево высотой 1"""
        result = gen_tree.gen_bin_tree(height = 1, root = 5)
        expected = {"root": 5, "left": None, "right": None}
        self.assertEqual(result, expected)

    def test_height_zero(self):
        """Тест: обработка нулевой высоты"""
        result = gen_tree.gen_bin_tree(height = 0, root = 5)
        self.assertEqual(result, {})

    def test_negative_height(self):
        """Тест: обработка отрицательной высоты"""
        result = gen_tree.gen_bin_tree(height=-1, root = 5)
        self.assertEqual(result, {})

    def test_negative_root(self):
        """Тест: работа с отрицательным значением корня"""
        result = gen_tree.gen_bin_tree(height = 2, root=-3)
        expected = {'root': -3, 'left': {'root': 9, 'left': None, 'right': None}, 'right': {'root': -5, 'left': None, 'right': None}}
        self.assertEqual(result, expected)

    def test_zero_root(self):
        """Тест: корень равен 0"""
        result = gen_tree.gen_bin_tree(height = 2, root = 0)
        expected = {'root': 0, 'left': {'root': 0, 'left': None, 'right': None}, 'right': {'root': -2, 'left': None, 'right': None}}
        self.assertEqual(result, expected)

    def test_large_root(self):
        """Тест: работа с большим значением корня"""
        result = gen_tree.gen_bin_tree(height = 2, root = 1000)
        expected ={'root': 1000, 'left': {'root': 1000000, 'left': None, 'right': None}, 'right': {'root': 998, 'left': None, 'right': None}}
        self.assertEqual(result, expected)

    def test_recursive_structure(self):
        """Тест: проверка целостности рекурсивной структуры дерева"""
        result = gen_tree.gen_bin_tree(height = 2, root = 2)
        self.assertEqual(result['root'], 2)
        self.assertEqual(result['left']['root'], 4)
        self.assertEqual(result['right']['root'], 0)

    def test_root_negative_large(self):
        """Тест: большое отрицательное значение корня"""
        result = gen_tree.gen_bin_tree(height = 2, root=-100)
        expected = {
        'root': -100, 'left': {'root': 10000, 'left': None, 'right': None}, 'right': {'root': -102, 'left': None, 'right': None}
        }
        self.assertEqual(result, expected)

    def test_root_fractional(self):
        """Тест: корень с дробной частью"""
        result = gen_tree.gen_bin_tree(height = 2, root = 5.0)
        expected = {
        'root': 5, 'left': {'root': 25, 'left': None, 'right': None}, 'right': {'root': 3, 'left': None, 'right': None}
        }
        self.assertEqual(result, expected)
        if __name__ == "__main__":
            unittest.main()
