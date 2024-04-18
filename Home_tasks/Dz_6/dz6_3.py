def is_prime(n): #Это объявление функции is_prime, которая принимает один аргумент n, предполагаемое простое число.
    if n <= 1: #Это проверка, является ли число n меньше или равным 1. Если да, то число не является простым, и функция возвращает False.
        return False
    for i in range(2, int(n**0.5) + 1): #Это цикл for, который будет итерироваться по значениям от 2 до целой части квадратного корня из n (включительно). Мы используем int(n**0.5) + 1, чтобы убедиться, что мы включаем в цикл последнее возможное делительное число.
        if n % i == 0: #Это проверка, делится ли число n на текущее значение i без остатка. Если делится, то число не является простым, и функция возвращает False.
            return False # Если в цикле было найдено делительное число, функция сразу возвращает False, так как число n не является простым.
        return True #Если в цикле не было найдено делительного числа, то число n является простым, и функция возвращает True.

#В этой части кода пользователь вводит число, которое нужно проверить, простое ли оно.
# Затем вызывается функция is_prime, и в зависимости от результата выводится соответствующее сообщение.
number = int(input("Введите числа: "))
if is_prime(number):
    print(number, "является простым числом")
else:
    print(number, "не является простым числом")