input_string = input("Введіть список цілих чисел, розділених пробілами: ")
numbers = list(map(int, input_string.split()))

min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print("Список з мінімальним і максимальним елементами, які помінялися місцями:")
print(numbers)
