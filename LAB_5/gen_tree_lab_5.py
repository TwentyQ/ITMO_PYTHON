from typing import Dict, Any, List


def gen_bin_tree(height: int = 6, root: int = 5,
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




