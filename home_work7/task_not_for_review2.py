numbers = list(map(int, input("Введіть список цілих чисел: ").split()))

positive_count = 0

for num in numbers:
    if num > 0:
        positive_count += 1

print(f"Кількість додатних елементів: {positive_count}")
