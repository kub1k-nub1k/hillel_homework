import random

n = int(input("Введіть розмір квадратної матриці: "))
matrix = [[random.randint(10, 99) for _ in range(n)] for _ in range(n)]

print("Матриця чисел:")
for row in matrix:
    print(row)

print()

dg_sum = sum(matrix[i][i] for i in range(n))
print("Сума чисел по діагоналі:", dg_sum)

last_num_sum = sum(row[n-1] for row in matrix)
print("Сума чисел останнього стовбця:", last_num_sum)
