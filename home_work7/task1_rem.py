numbers = list(range(10, 251))

for n in numbers:
    if n % 20 == 0:
        numbers.remove(n)

print(numbers)
