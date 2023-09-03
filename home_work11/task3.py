def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def prime_generator(N, Z):
    for number in range(max(N, 2), Z + 1):
        if is_prime(number):
            yield number


N = int(input("Введіть початкове значення діапазону N: "))
Z = int(input("Введіть кінцеве значення діапазону Z: "))

prime_numbers = list(prime_generator(N, Z))
print("Прості числа в діапазоні від", N, "до", Z, ":", prime_numbers)
