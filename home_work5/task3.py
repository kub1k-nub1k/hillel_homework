user_input = input("Введіть число від 3 до 9: ")

if user_input.isdigit():
    number = int(user_input)
    if 3 <= number <= 9:
        print("\nВирівнювання по лівому краю:")
        for i in range(1, number + 1):
            row = ''.join(str(j) for j in range(1, i + 1))
            row += row[-2::-1]
            print(row)

        print("\nЦентрування:")
        for i in range(1, number + 1):
            row = ''.join(str(j) for j in range(1, i + 1))
            row += row[-2::-1]
            print(row.center(number * 2 - 1))

        print("\nВирівнювання по правому краю:")
        for i in range(1, number + 1):
            row = ''.join(str(j) for j in range(1, i + 1))
            row += row[-2::-1]
            print(row.rjust(number * 2 - 1))


    else:
        print("Помилка: Введіть число в діапазоні від 3 до 9.")
else:
    print("Помилка: Необхідно ввести число")
