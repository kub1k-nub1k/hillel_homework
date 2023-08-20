input_string = input("Введіть послідовність цілих чисел, розділених пробілами: ")
numbers = list(map(int, input_string.split()))

last_two = numbers[-2:]
numbers = last_two + numbers[:-2]

print("Список з переміщеними двома останніми елементами на початок:")
print(numbers)
