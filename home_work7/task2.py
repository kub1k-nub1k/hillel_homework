sentence = input("Введіть речення більше ніж з двох слів: ")

words_list = sentence.split(" ")

words_list = [word for word in words_list if word]

print("{:<10} {:<10}".format("Індекс", "Слово"))
for index, word in enumerate(words_list):
    print("{:<10} {:<10}".format(index, word))

print("Кількість слів:", len(words_list))


