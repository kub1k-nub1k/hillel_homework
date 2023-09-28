N = int(input("Введите число N: "))

number = 1

while number <= N:
    factor = number * number
    if factor <= N:
        print(factor)
        number += 1
