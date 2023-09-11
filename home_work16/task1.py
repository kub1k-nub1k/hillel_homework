with open("text.txt", "a") as file:
    while True:
        user_input = input("Введіть текст (порожній рядок для завершення: ")

        if user_input == "":
            break

        file.write(user_input + '\n')

print('Дані були записані у файл: "text.txt"')


