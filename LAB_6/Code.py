import timeit
import matplotlib.pyplot as plt
import random
from typing import Dict, Any, List

"""Бинарное дерево рекурсивным методом"""


def build_tree_recursive(height: int = 6, root: int = 5) -> Dict[str, Any]:
    """
    Создает бинарное дерево в виде словаря.

    Ключевые аргументы:
    height -- высота дерева
    root -- число в корне дерева

    Возвращает:
    dict -- бинарное дерево в виде словаря
    """

    # Если высота меньше 1, возвращается пустой словарь
    if height < 1:
        return {}

    # Если достигнута конечная высота, возвращает текущее значение узла
    if height == 1:
        return {"root": root, "left": None, "right": None}

    # Вычисляем дочерние ветви
    left_child = root ** 2  # Вычисляет левые ветви как квадрат корня
    right_child = root - 2  # Вычисляет правые ветви как корень минус 2

    # Формируем узел дерева: текущее значение + две ветки-потомка
    return {
        # Текущее значение узла
        "root": root,

        # Левая ветка: уменьшаем высоту, вычисляем новое значение
        "left": build_tree_recursive(height - 1, left_child),

        # Правая ветка: уменьшаем высоту, вычисляем новое значение
        "right": build_tree_recursive(height - 1, right_child)

    }


"""Бинарное дерево нерекурсивным методом"""


def build_tree_iterative(height: int = 6, root: int = 5,
                         left_branch=lambda l_r: l_r ** 2,
                         right_branch=lambda r_r: r_r - 2) -> Dict[str, Any]:
    """
    Нерекурсивное построение бинарного дерева.

    Ключевые аргументы:
        height: Высота дерева
        root: Значение корня
        left_branch: Функция для левого потомка (по умолчанию root^2)
        right_branch: Функция для правого потомка (по умолчанию root-2)

    Возвращает:
        dict -- бинарное дерево в виде словаря
    """

    # Создаем корневой узел
    tree: Dict[str, Any] = {"root": root}

    # Если высота меньше 1, возвращается пустой словарь
    if height < 1:
        return {}

    # Если высота = 1, возвращаем только корень
    if height == 1:
        return tree

    # Список для хранения узлов текущего уровня дерева
    level: List[Dict[str, Any]] = [tree]

    # Строим дерево уровень за уровнем
    for depth in range(2, height + 1):
        level_new: List[Dict[str, Any]] = []  # Узлы следующего уровня

        # Обработка каждого узла текущего уровня
        for element in level:
            # Создание левой ветви

            # Вычисление значения для левой ветви с помощью пользовательской функции
            left_value = left_branch(element["root"])

            # Создание нового узла-потомка
            left_dict = {"root": left_value}

            # Присоединение левой ветви к текущему узлу
            element["left"] = left_dict

            # Сохранение новой левой ветви для дальнейших уровней
            level_new.append(left_dict)

            # Создание правой ветви

            # Вычисление значения для правой ветви с помощью пользовательской функции
            right_value = right_branch(element["root"])

            # Создание нового узла-потомка
            right_dict = {"root": right_value}

            # Присоединение правой ветви к текущему узлу
            element["right"] = right_dict

            # Сохранение новой правой ветви для дальнейших уровней
            level_new.append(right_dict)

        # Переход на следующий уровень
        level = level_new

    # Возвращаем корневой узел, который содержит всё дерево
    return tree


def benchmark(func, height, root=5, repeat=100):
    """Возвращает среднее время выполнения func(n)"""
    times = timeit.repeat(lambda: func(height, root), number=1, repeat=repeat)
    return min(times)


"""Построение графика"""


def main():
    # Фиксированный набор данных
    random.seed(42)
    test = list(range(1, 18, 2))  # Список тестовых высот деревьев

    # Списки для хранения результатов измерений
    res_recursive = []  # Время для рекурсивного метода
    res_iterative = []  # Время для итеративного метода

    # Измерение времени выполнения для каждой высоты дерева
    for n in test:
        res_iterative.append(benchmark(build_tree_iterative, n))
        res_recursive.append(benchmark(build_tree_recursive, n))

    # Визуализация графика
    plt.plot(test, res_recursive, label="Рекурсивный")  # Линия рекурсивного метода
    plt.plot(test, res_iterative, label="Нерекурсивный")  # Линия итеративного метода
    plt.xlabel("Высота дерева")  # Подпись оси х
    plt.ylabel("Время построения дерева (сек)")  # Подпись оси у
    plt.title("Сравнение двух подходов построения бинарного дерева")  # Заголовок
    plt.legend()  # Легенда

    plt.tight_layout()  # Оптимизация графика
    plt.show()  # Показ графика


if __name__ == "__main__":
    main()
