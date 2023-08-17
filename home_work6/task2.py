print("Загадайте число від 0 до 100.")
print("Програма буде намагатися вгадати його.")

ready = input("Готові? (так/ні): ")
if ready != "так":
    print("Ок, звертайтесь, якщо захочете грати.")
else:
    lower_bound = 0
    upper_bound = 100
    target_number = (lower_bound + upper_bound) // 2
    steps = 1
    guessed = False

    while not guessed and lower_bound <= upper_bound:
        response = input(f"""Чи це ваше число {target_number}? 
Варіанти відповіді: більше/меньше/це воно: """)

        if response == "більше":
            lower_bound = target_number + 1
            distance = upper_bound - lower_bound
            target_number = lower_bound + distance // 2
        elif response == "меньше":
            upper_bound = target_number - 1
            distance = upper_bound - lower_bound
            target_number = upper_bound - distance // 2
        elif response == "це воно":
            guessed = True
        else:
            print("Ви ввели некоректну відповідь. Введіть 'більше', 'меньше' або 'це воно'.")

        steps += 1

    if guessed:
        print(f"Програма вгадала ваше число {target_number} за {steps} спроб.")
    else:
        print("Ви граєте не чесно!")
