check_year = int(input("Введите год для проверки:"))

if check_year < 1899 or check_year > 1_000_001:
    print("Число не подходит по условию проверки")
else:
    if (check_year % 4 == 0 and check_year % 100 != 0) or (check_year % 400 == 0):
        print(check_year, "- высокосный год")
    else:
        print(check_year, " - не высокосный")
