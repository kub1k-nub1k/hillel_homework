# Замена значений переменных "num_1" и "num_2" с использованием третьей переменной "num_3"
print("Task #1")

num_1 = 5
num_2 = 10

print("Исходные данные")
print("num_1=", num_1)
print("num_2=", num_2)

num_3 = num_1
num_1 = num_2
num_2 = num_3

print("Измененные данные")
print("num_1=", num_1)
print("num_2=", num_2)


# Замена значений переменных "num_1" и "num_2" с использованием свойств Python
print()
print("Task #2")

num_1 = 5
num_2 = 10

print("Исходные данные")
print("num_1=", num_1)
print("num_2=", num_2)

num_1, num_2 = num_2, num_1

print("Измененные данные")
print("num_1=", num_1)
print("num_2=", num_2)

# Замена значений переменных "num_1" и "num_2" с использованием альтернативного способа
print()
print("Task #3")

num_1 = 5
num_2 = 10

print("Исходные данные")
print("num_1=", num_1)
print("num_2=", num_2)

num_2 = num_2 - num_1
num_1 = num_1 + num_1

print("Измененные данные")
print("num_1=", num_1)
print("num_2=", num_2)
