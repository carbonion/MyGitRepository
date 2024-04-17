def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
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
