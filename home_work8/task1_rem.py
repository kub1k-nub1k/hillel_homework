n = int(input("Введіть розмір квадратної матриці: "))
matrix = [[i if i % 2 == 0 else j - n + 1 for j in range(n)] for i in range(n)]

print("Варіант №1")
for row in matrix:
    formatted_row = "  ".join(f"{num:>3}" for num in row)
    print(f"[{formatted_row}]")

print("Варіант №2")
for num in matrix:
    print(" ".join(f"{num:>3}" for num in num))

print("Варіант №3")  #розпакування масиву, яке ви показували на уроці
print(*matrix, sep="\n")

print("Варіант №4")
for r in matrix:
    print(r)
