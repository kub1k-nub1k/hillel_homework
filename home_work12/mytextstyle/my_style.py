def text_style(text, style='normal'):
    styles = {
        'normal': '0',
        'bold': '1',
        'italic': '3',
    }
    return f'\033[{styles.get(style, "0")}m{text}\033[0m'

def text_color(text, color='white'):
    colors = {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'purple': '35',
        'cyan': '36',
        'white': '37',
    }
    return f'\033[{colors.get(color, "37")}m{text}\033[0m'

def background_color(text, bg_color='black'):
    bg_colors = {
        'black': '40',
        'red': '41',
        'green': '42',
        'yellow': '43',
        'blue': '44',
        'purple': '45',
        'cyan': '46',
        'white': '47',
    }
    return f'\033[{bg_colors.get(bg_color, "40")}m{text}\033[0m'



