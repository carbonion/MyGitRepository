'''Объявление функции binary_search_recursive с четырьмя аргументами:
arr - отсортированный список чисел,
target - значение, которое мы ищем в списке,
left и right - границы интервала поиска.'''
def binary_search_recursive(arr, target, left, right):
    '''Проверка, если левая граница интервала больше правой, т.е. интервал пуст, и возвращается -1.'''
    if left > right:
        return -1

    mid = (left + right) // 2 '''Вычисление середины интервала поиска.'''

    '''Проверка, если элемент в середине интервала равен целевому значению, возвращается его позиция.'''
    if arr[mid] == target:
        return mid

    '''Проверка, если элемент в середине интервала меньше целевого значения, рекурсивный вызов функции для правой половины интервала.'''
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)

    '''В противном случае рекурсивный вызов функции для левой половины интервала.'''
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# Пример списка чисел
numbers = [1, 3, 3, 7, 9, 13, 57, 69, 88, 121]

# Искомое значение
target = 88

# Используем рекурсивный бинарный поиск:
position = binary_search_recursive(numbers, target, 0, len(numbers) - 1)

# Выводим результат:
if position != -1:
    print("Элемент", target, "найден на позиции", position)
else:
    print("Элемент", target, "не найден в списке")
