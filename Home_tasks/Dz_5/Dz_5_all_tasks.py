# Первая формула, sin:

import math


def calculate_sin(x, n_terms):
    result = 0
    for n in range(n_terms):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        result += term
    return result


# Установим значение x и количество терминов (членов ряда)
x = 1  # Пример значения x
n_terms = 10  # Пример количества терминов ряда

# Вычислим sin(x) с использованием суммы ряда
sin_x = calculate_sin(x, n_terms)

print("sin({}) ≈ {:.5f}".format(x, sin_x))

# Вторая формула, cos:
import math


def calculate_cos(x, n_terms):
    result = 0
    for n in range(n_terms):
        term = ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
        result += term
    return result


# Установим значение x и количество терминов (членов ряда)
x = 1  # Пример значения x
n_terms = 10  # Пример количества терминов ряда

# Вычислим cos(x) с использованием суммы ряда
cos_x = calculate_cos(x, n_terms)

print("cos({}) ≈ {:.5f}".format(x, cos_x))


# Задача про Машу:
def days_to_save(N, k):
    saved_money = 0
    days = 0

    while saved_money < N:
        days += 1
        if days % 7 != 0:  # Проверяем, не воскресенье ли сегодня
            saved_money += k

    return days


# Пример использования функции
N = 1000  # Цена телефона
k = 50  # Сколько Маша откладывает в день

days_needed = days_to_save(N, k)
print("Маше потребуется {} дней для накопления {} рублей.".format(days_needed, N))


# Числа Фибоначчи:
def fibonacci_sequence(n):
    # Инициализируем первые два числа Фибоначчи
    fibonacci_numbers = [1, 1]

    # Генерируем последующие числа Фибоначчи
    for i in range(2, n):
        next_number = fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2]
        fibonacci_numbers.append(next_number)

    return fibonacci_numbers


# Выводим первые 10 чисел Фибоначчи
n = 10
fibonacci_numbers = fibonacci_sequence(n)
print("Первые {} чисел Фибоначчи:".format(n), fibonacci_numbers)


# Список чисел, Min and Max:
def calculate_statistics(numbers):
    if not numbers:
        return None, None, None

    total = sum(numbers)
    min_number = min(numbers)
    max_number = max(numbers)

    return total, min_number, max_number


# Пример списка чисел
numbers = [10, 5, 20, 15, 30]

# Вычисление статистики
total, min_number, max_number = calculate_statistics(numbers)

# Вывод результатов
print("Сумма чисел:", total)
print("Минимальное число:", min_number)
print("Максимальное число:", max_number)


# Уникальность чисел:
def check_uniqueness(numbers):
    # Создаем словарь для подсчета повторяющихся элементов
    counts = {}

    # Проверяем уникальность элементов
    unique = True
    for num in numbers:
        if num in counts:
            counts[num] += 1
            unique = False
        else:
            counts[num] = 1

    return unique, counts


# Пример списка чисел
numbers = [1, 2, 3, 4, 5, 3, 7, 8, 9, 10]

# Проверка уникальности чисел
is_unique, duplicates = check_uniqueness(numbers)

# Вывод результатов
if is_unique:
    print("Все числа в списке уникальны.")
else:
    print("Не все числа в списке уникальны.")
    print("Дублирующиеся элементы и их количество повторений:")
    for num, count in duplicates.items():
        if count > 1:
            print("Число:", num, "Повторений:", count)


# Бинарный поиск:
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Пример списка чисел
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Значение, которое мы ищем в списке
target = 11

# Выполняем бинарный поиск
position = binary_search(numbers, target)

# Выводим результат
if position != -1:
    print("Элемент", target, "найден на позиции", position)
else:
    print("Элемент", target, "не найден в списке")


# Бинарный поиск по сдвинутому списку:
def binary_search_rotated(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# Пример сдвинутого списка чисел
rotated_numbers = [5, 6, 7, 1, 2, 3, 4]

# Значение, которое мы ищем в списке
target = 2

# Выполняем бинарный поиск
position = binary_search_rotated(rotated_numbers, target)

# Выводим результат
if position != -1:
    print("Элемент", target, "найден на позиции", position)
else:
    print("Элемент", target, "не найден в списке")
