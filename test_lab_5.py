import unittest  # Импорт модуля для тестов
import gen_tree_lab_5  # Импорт пользовательского модуля


class TestTree(unittest.TestCase):
    """Тесты для функции gen_bin_tree (вариант 5)"""

    def test_var_5(self):
        """Тест: вариант 5(Root = 5, height = 6,
                            left_branch = root^2,
                            right_branch = root-2)
        """
        result = gen_tree_lab_5.gen_bin_tree(height=6, root=5,
                                             left_branch=lambda l_r: l_r ** 2,
                                             right_branch=lambda r_r: r_r - 2)
        expected = {'root': 5, 'left': {'root': 25, 'left': {'root': 625, 'left': {'root': 390625,
                                                                                   'left': {'root': 152587890625,
                                                                                            'left': {
                                                                                                'root': 23283064365386962890625},
                                                                                            'right': {
                                                                                                'root': 152587890623}},
                                                                                   'right': {'root': 390623, 'left': {
                                                                                       'root': 152586328129}, 'right': {
                                                                                       'root': 390621}}},
                                                             'right': {'root': 623, 'left': {'root': 388129, 'left': {
                                                                 'root': 150644120641}, 'right': {'root': 388127}},
                                                                       'right': {'root': 621, 'left': {'root': 385641},
                                                                                 'right': {'root': 619}}}},
                                        'right': {'root': 23, 'left': {'root': 529, 'left': {'root': 279841, 'left': {
                                            'root': 78310985281}, 'right': {'root': 279839}},
                                                                       'right': {'root': 527, 'left': {'root': 277729},
                                                                                 'right': {'root': 525}}},
                                                  'right': {'root': 21, 'left': {'root': 441, 'left': {'root': 194481},
                                                                                 'right': {'root': 439}},
                                                            'right': {'root': 19, 'left': {'root': 361},
                                                                      'right': {'root': 17}}}}}, 'right': {'root': 3,
                                                                                                           'left': {
                                                                                                               'root': 9,
                                                                                                               'left': {
                                                                                                                   'root': 81,
                                                                                                                   'left': {
                                                                                                                       'root': 6561,
                                                                                                                       'left': {
                                                                                                                           'root': 43046721},
                                                                                                                       'right': {
                                                                                                                           'root': 6559}},
                                                                                                                   'right': {
                                                                                                                       'root': 79,
                                                                                                                       'left': {
                                                                                                                           'root': 6241},
                                                                                                                       'right': {
                                                                                                                           'root': 77}}},
                                                                                                               'right': {
                                                                                                                   'root': 7,
                                                                                                                   'left': {
                                                                                                                       'root': 49,
                                                                                                                       'left': {
                                                                                                                           'root': 2401},
                                                                                                                       'right': {
                                                                                                                           'root': 47}},
                                                                                                                   'right': {
                                                                                                                       'root': 5,
                                                                                                                       'left': {
                                                                                                                           'root': 25},
                                                                                                                       'right': {
                                                                                                                           'root': 3}}}},
                                                                                                           'right': {
                                                                                                               'root': 1,
                                                                                                               'left': {
                                                                                                                   'root': 1,
                                                                                                                   'left': {
                                                                                                                       'root': 1,
                                                                                                                       'left': {
                                                                                                                           'root': 1},
                                                                                                                       'right': {
                                                                                                                           'root': -1}},
                                                                                                                   'right': {
                                                                                                                       'root': -1,
                                                                                                                       'left': {
                                                                                                                           'root': 1},
                                                                                                                       'right': {
                                                                                                                           'root': -3}}},
                                                                                                               'right': {
                                                                                                                   'root': -1,
                                                                                                                   'left': {
                                                                                                                       'root': 1,
                                                                                                                       'left': {
                                                                                                                           'root': 1},
                                                                                                                       'right': {
                                                                                                                           'root': -1}},
                                                                                                                   'right': {
                                                                                                                       'root': -3,
                                                                                                                       'left': {
                                                                                                                           'root': 9},
                                                                                                                       'right': {
                                                                                                                           'root': -5}}}}}}
        self.assertEqual(result, expected)

    def test_height_1(self):
        """Тест: дерево высотой 1"""
        result = gen_tree_lab_5.gen_bin_tree(height=1, root=5,
                                             left_branch=lambda l_r: l_r ** 2,
                                             right_branch=lambda r_r: r_r - 2)
        expected = {"root": 5}
        self.assertEqual(result, expected)

    def test_height_zero(self):
        """Тест: обработка нулевой высоты"""
        result = gen_tree_lab_5.gen_bin_tree(height=0, root=5,
                                             left_branch=lambda l_r: l_r ** 2,
                                             right_branch=lambda r_r: r_r - 2)
        self.assertEqual(result, {})

    def test_negative_height(self):
        """Тест: обработка отрицательной высоты"""
        result = gen_tree_lab_5.gen_bin_tree(height=-1, root=5,
                                             left_branch=lambda l_r: l_r ** 2,
                                             right_branch=lambda r_r: r_r - 2)
        self.assertEqual(result, {})

    def test_negative_root(self):
        """Тест: работа с отрицательным значением корня"""
        result = gen_tree_lab_5.gen_bin_tree(height=2, root=-3,
                                             left_branch=lambda l_r: l_r ** 2,
                                             right_branch=lambda r_r: r_r - 2)
        expected = {'root': -3, 'left': {'root': 9},
                    'right': {'root': -5}}
        self.assertEqual(result, expected)

    def test_zero_root(self):
        """Тест: корень равен 0"""
        result = gen_tree_lab_5.gen_bin_tree(height=2, root=0,
                                             left_branch=lambda l_r: l_r ** 2,
                                             right_branch=lambda r_r: r_r - 2)
        expected = {'root': 0, 'left': {'root': 0},
                    'right': {'root': -2}}
        self.assertEqual(result, expected)

    def test_large_root(self):
        """Тест: работа с большим значением корня"""
        result = gen_tree_lab_5.gen_bin_tree(height=2, root=1000,
                                             left_branch=lambda l_r: l_r ** 2,
                                             right_branch=lambda r_r: r_r - 2)
        expected = {'root': 1000, 'left': {'root': 1000000},
                    'right': {'root': 998}}
        self.assertEqual(result, expected)

    def test_root_negative_large(self):
        """Тест: большое отрицательное значение корня"""
        result = gen_tree_lab_5.gen_bin_tree(height=2, root=-100,
                                             left_branch=lambda l_r: l_r ** 2,
                                             right_branch=lambda r_r: r_r - 2)
        expected = {
            'root': -100, 'left': {'root': 10000},
            'right': {'root': -102}
        }
        self.assertEqual(result, expected)

    def test_root_fractional(self):
        """Тест: корень с дробной частью"""
        result = gen_tree_lab_5.gen_bin_tree(height=2, root=5.0,
                                             left_branch=lambda l_r: l_r ** 2,
                                             right_branch=lambda r_r: r_r - 2)
        expected = {
            'root': 5, 'left': {'root': 25},
            'right': {'root': 3}
        }

        self.assertEqual(result, expected)

    def test_user_func(self):
        """Тест: пользовательские функции"""
        result = gen_tree_lab_5.gen_bin_tree(height=3, root=66,
                                             left_branch=lambda l_r: l_r + 6,
                                             right_branch=lambda r_r: r_r - 6)
        expected = {
            'root': 66, 'left': {'root': 72, 'left': {'root': 78}, 'right': {'root': 66}},
            'right': {'root': 60, 'left': {'root': 66}, 'right': {'root': 54}}
        }

        self.assertEqual(result, expected)

    def test_hard_user_func(self):
        """Тест: более сложные пользовательские функции"""
        result = gen_tree_lab_5.gen_bin_tree(height=3, root=66,
                                             left_branch=lambda l_r: l_r % 6,
                                             right_branch=lambda r_r: r_r ** 0.2)
        expected = {
            'root': 66, 'left': {'root': 0, 'left': {'root': 0}, 'right': {'root': 0.0}},
            'right': {'root': 2.311579248730029, 'left': {'root': 2.311579248730029},
                      'right': {'root': 1.1824472005401296}}
        }

        self.assertEqual(result, expected)

    def test_negative_func(self):
        """Тест: функции с отрицательными значениями"""
        result = gen_tree_lab_5.gen_bin_tree(height=2, root=5,
                                             left_branch=lambda l_r: -l_r,
                                             right_branch=lambda r_r: -r_r * 2)
        expected = {
            'root': 5, 'left': {'root': -5}, 'right': {'root': -10}
        }
        self.assertEqual(result, expected)

    def test_zero_func(self):
        """Тест: функции с нулём"""
        result = gen_tree_lab_5.gen_bin_tree(height=2, root=1000,
                                             left_branch=lambda l_r: 0,
                                             right_branch=lambda r_r: 0)
        expected = {
            'left': {'root': 0}, 'right': {'root': 0}, 'root': 1000
        }
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
