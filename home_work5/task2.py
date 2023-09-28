rows = int(input("Введіть кількість рядків: "))

for i in range(1, rows + 1):
    zeros = '0' * (i - 1)
    number = '1' + zeros
    print("{:>3}: {:>4}".format(i - 1, number.rjust(rows)))
