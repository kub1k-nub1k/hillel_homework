list1 = [1, 2, 3, 4, 5, 6]
list2 = [9, 8, 5, 6, 7, 3]
count = len(set(list1) & set(list2))
print(f"Кількість спільних різних чисел: {count}")
