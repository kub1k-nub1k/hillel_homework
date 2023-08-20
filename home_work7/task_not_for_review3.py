input_list = input("Введіть список чисел через пробіл: ")
numbers = input_list.split()

unique_numbers = []

for num in numbers:
    num = int(num)
    if numbers.count(str(num)) == 1:
        unique_numbers.append(num)

print("Елементи без повторень:", unique_numbers)
