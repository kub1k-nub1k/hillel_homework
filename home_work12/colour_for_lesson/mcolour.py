colour = {
    'red': '31m',
    'black': '30m',
    'green': '32m',
    'yellow': '33m',
    'blue': '34m',
    'purpure': '35m',
    'biruza': '36m',
    'white': '37m'
}

def color_text(text: str, colour_name: str) -> str:
    """
    Забарвлює текст у вказаний колір.

    :param text: Текст, який потрібно забарвити.
    :param colour_name: Назва кольору зі словника 'colour'.
    :return: Забарвлений текст.
    """
    coloured_txt = '\033[' + colour_name + text + '\033[0m'
    return coloured_txt

def styled(text: str, code: str = "3m") -> str:
    """
    Застосовує стилі до тексту.

    :param text: Текст, до якого потрібно застосувати стилі.
    :param code: Код стилю (за замовчуванням - "3m").
    :return: Текст з застосованими стилями.
    """
    clean_style_code = '\033[0m'
    styled_txt = f'\033[{code}{text}{clean_style_code}'
    return styled_txt

def error_message(message: str) -> str:
    """
    Генерує повідомлення про помилку.

    :param message: Текст повідомлення.
    :return: Забарвлене повідомлення про помилку.
    """
    status = "ERROR"
    error = color_text(f"{status:<8} ", colour['red'])
    _message = color_text(message, colour['yellow'])
    err_message = error + _message
    return err_message

def warning_message(message: str) -> str:
    """
    Генерує попередження.

    :param message: Текст повідомлення.
    :return: Забарвлене попередження.
    """
    status = "WARNING"
    warn = color_text(f"{status:<8} ", colour['yellow'])
    _message = color_text(message, colour['biruza'])
    warn_message = warn + _message
    return warn_message

def info_message(message: str) -> str:
    """
    Генерує інформаційне повідомлення.

    :param message: Текст повідомлення.
    :return: Забарвлене інформаційне повідомлення.
    """
    status = "INFO"
    info = color_text(f"{status:<8} ", colour['purpure'])
    info_message = info + message
    return info_message

if __name__ == "__main__":
    print(warning_message("ups i did sit again"))
    print(error_message("wrong way"))
    print(info_message("thanks for info"))
