list1 = [1, 2, 5, 7, 9, 99, 87, 200, 39, 2]
list2 = [5, 42, 29, 345, 50, 33, 7, 0, 201, 9, 2, 132, 45, 23, 934]

count_dict1 = {}
count_dict2 = {}

for num in list1:
    if num in list2:
        if num in count_dict1:
            count_dict1[num] += 1
        else:
            count_dict1[num] = 1

print("Повторення в списку №1")
print("{:<10} {:<10}".format("Число", "Кількість"))
for num, count in count_dict1.items():
    print("{:<10} {:<10}".format(num, count))

for num in list2:
    if num in list1:
        if num in count_dict2:
            count_dict2[num] += 1
        else:
            count_dict2[num] = 1


print("Повторення в списку №2")
print("{:<10} {:<10}".format("Число", "Кількість"))
for num, count in count_dict2.items():
    print("{:<10} {:<10}".format(num, count))