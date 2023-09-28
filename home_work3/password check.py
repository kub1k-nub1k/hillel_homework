password = input("Придумайте ваш пароль:")
checkout = input("Введите ваш пароль для проверки:")

if password == checkout:
    print("Ваш пароль принято")
else:
    print("Вы указали неправильный пароль")