n = int(input("Введіть кількість рядків: "))
m = int(input("Введіть кількість стовпців: "))

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            print(".", end=" ")
        else:
            print("*", end=" ")
    print()
