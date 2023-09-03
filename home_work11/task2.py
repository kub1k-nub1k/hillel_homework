f1 = lambda x, y=1: x ** y

list1 = [1, 2, 3, 4]
result = list(map(f1, list1))

print("Тест №1: Вхідний список:", list1)
print("Результат №1:", result)
print()

list2 = [2, 3, 4, 5]
list3 = [1, 2, 3, 4]
result = list(map(f1, list2, list3))

print("Тест №2: Вхідний список 1:", list2)
print("Тест №2: Вхідний список 2:", list3)
print("Результат №2:", result)
