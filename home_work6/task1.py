string = input("Введіть рядок: ")
char = input("Введіть символ: ")

found_index = string.find(char)

while found_index != -1:
    print(f"Символ '{char}' знаходиться на позиції: {found_index}")
    found_index = string.find(char, found_index + 1)
