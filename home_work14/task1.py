def password_requirements(func):
    def wrapper(*args, **kwargs):
        while True:
            password = input("Введіть пароль: ")
            is_valid, message = is_valid_password(password)

            if is_valid:
                return func(password, *args, **kwargs)
            else:
                print(f"Помилка: Пароль не відповідає вимогам. {message}")

    return wrapper


def is_valid_password(password):
    if not password:
        return False, "Пароль не може бути пустим."

    if any(char.isspace() for char in password):
        return False, "Пароль не може містити пробіли або табуляцію."

    if len(password) < 8:
        return False, "Пароль повинен бути не менше 8 символів."

    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        return False, "Пароль повинен містити хоча б одну цифру."

    has_letter = any(char.isalpha() for char in password)
    if not has_letter:
        return False, "Пароль повинен містити хоча б одну букву."

    special_chars = "!@#$%^&*()-_+="
    has_special = any(char in special_chars for char in password)
    if not has_special:
        return False, "Пароль повинен містити хоча б один спеціальний символ."

    return True, ""


@password_requirements
def process_password(password):
    print("Ваш пароль:", password)


process_password()
