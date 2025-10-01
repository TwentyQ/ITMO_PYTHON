def main():
    """
       Основная функция для взаимодействия с пользователем через консоль.
    """

    # Запрос числа у пользователя
    target = int(input('Загадайте число:'))

    # Запрос типа алгоритма поиска у пользователя
    search_var = (input('Желаемый метод поиска(seq -  медленный перебор, bin -  бинарного поиска):'))

    # Запрос типа диапазон у пользователя
    chooserange0 = int(input(
        'Если вы хотите задать последовательный диапазон, то напишите 1, если задать с помощью клавиатуры, напишите 2: '))
    if chooserange0 == 2: # Выбран диапазон с клавиатуры
        chooserange = list(map(int, input('Введите числа через запятую:').split(','))) # Формирование диапазона
        return guess_number(target, chooserange, type=search_var) # Вывод результата
    else: # Выбран диапазон с известным началом и концом
        chooserange1 = list(map(int, input('Введите диапазон через запятую (от,до):').split(',')))
        chooserange = []
        for x in range(chooserange1[0], chooserange1[1] + 1): # Формирование диапазона
            chooserange.append(x)
        return guess_number(target, chooserange, type=search_var) # Вывод результата


def guess_number(target: int, chooserange: list, type: str) -> list[int, int | None]:
    """
    Угадывает заданное число в указанном диапазоне с использованием выбранного алгоритма.

    Ключевые аргументы:
    target -- число, которое нужно угадать
    chooserange -- диапазон чисел для поиска
    type -- алгоритм поиска ('seq' - последовательный, 'bin' - бинарный)

    Возвращает:
    list -- список, содержащий:
        - угаданное число (или исходное target, если не найдено)
        - количество попыток (или None, если число не найдено)
    """

    if type == 'seq': # Выбран последовательный тип поиска
        chooserange.sort() # Сортировка диапазона
        tries = 0 # Счётчик попыток
        for x in chooserange:
            tries += 1
            if x == target:
                return [x, tries] # Число найдено
        return [target, None] # Число не найдено

    if type == 'bin': # Выбран последовательный тип поиска
        chooserange.sort() # Сортировка диапазона
        left_part = 0 # Левая часть диапазона (до медианы)
        right_part = len(chooserange) - 1 # Правая часть диапазона (после медианы)
        tries = 0 # Счётчик попыток

        while left_part <= right_part:
            middle = (left_part + right_part) // 2 # Находи медиану
            tries += 1
            if chooserange[middle] == target:
                return [chooserange[middle], tries] # Число найдено
            elif chooserange[middle] < target:
                left_part = middle + 1 # Ищем в правой части
            else:
                right_part = middle - 1 # Ищем в левой части

        return [target, None] # Число не найдено
    return [target, None] # Пользователь указал неизвестный тип поиска

