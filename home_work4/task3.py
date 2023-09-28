sum = 0
count = 0
max_value = None
min_value = None
even_count = 0
odd_count = 0

while True:
    num = int(input('Введите число (введите "0" для завершения): '))
    if num == 0:
        break

    sum += num
    count += 1
    if max_value is None or num> max_value:
        max_value = num
    if min_value is None or num< min_value:
        min_value = num
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if count > 0:
    average = sum / count
else:
    average = 0

print("Сума чисел:", sum)
print("среднее арифметическое:", average)
print("Максимальное значение:", max_value)
print("Минимальное значение:", min_value)
print("Количество парных чисел:", even_count)
print("Количество непарных чисел:", odd_count)