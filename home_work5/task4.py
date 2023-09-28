# для перевірки abcdefghijklmnopqrstuvwxyz
user_input = input("Введіть рядок (більше 15 символів): ")

if len(user_input) < 15:
    print("Рядок повинен містити щонайменше 15 символів")
else:
    print("Третій символ:", user_input[2])

    print("Передостанній символ:", user_input[-2])

    print("Перші п'ять символів:", user_input[:5])

    print("Весь рядок, крім двох останніх символів:", user_input[:-2])

    print("Символи з парними індексами:", user_input[::2])

    print("Символи з непарними індексами:", user_input[1::2])

    print("Символи у зворотному порядку:", user_input[::-1])

    print("Символи через один у зворотному порядку:", user_input[-1::-2])

    print("Довжина рядка:", len(user_input))
