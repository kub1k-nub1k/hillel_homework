import random
random_dict = {f'key_{i}': random.randint(1, 10) for i in range(20)}

product = 1
for value in random_dict.values():
    product *= value

print("Сгенерований словник:")
for key, value in random_dict.items():
    print(f'Ключ: {key}, Значення: {value}')

print()
print("Результат множення чисел:", product)
