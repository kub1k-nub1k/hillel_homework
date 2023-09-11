def sum_or_concatenate():
    try:
        num1 = input("Введіть перше число: ")
        num2 = input("Введіть друге число: ")

        num1 = float(num1)
        num2 = float(num2)

        result = num1 + num2
        print(f"Сума чисел: {result}")

    except ValueError:
        num1 = str(num1)
        num2 = str(num2)

        result = num1 + num2
        print(f"Результат конкатенації: {result}")

if __name__ == "__main__":
    sum_or_concatenate()
