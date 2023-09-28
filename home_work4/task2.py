N = int(input("Введите число N: "))

number = 1

while number <= N:
    square = number ** 2
    divisor = 1
    while divisor <= number:
        divisor *= 10
    last_number = square % divisor
    if last_number == number:
        print(number)
    number += 1