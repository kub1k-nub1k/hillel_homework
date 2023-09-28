user_number = input("Введите число: ")

dublicate = False
line = 0

while line < 10:
    сount = 0
    for i in user_number:
        if i == str(line):
            сount += 1
            if сount >= 2:
                dublicate = True
                break
    if dublicate:
        break
    line += 1

if dublicate:
    print("Есть повторения")
else:
    print("Повторений нет")
