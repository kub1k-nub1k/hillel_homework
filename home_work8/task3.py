import random

numbers = [random.randint(11, 99) for _ in range(15)]

even_sum = sum(num for num in numbers if num % 2 == 0)
odd_sum = sum(num for num in numbers if num % 2)

if odd_sum > even_sum:
    print("Так")
else:
    print("Ні")
