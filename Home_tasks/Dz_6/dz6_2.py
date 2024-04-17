def decimal_to_binary_iterative(decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    return binary

# Пример:
decimal_number = int(input("Введите числе в десятичной системе счисления: "))
binary_number = decimal_to_binary_iterative(decimal_number)
print("Двоичное представление числа:", binary_number)