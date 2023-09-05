from mytextstyle.my_style import text_style, text_color, background_color

header = "Любіть Україну"
text = """Любіть Україну, як сонце любіть,
як вітер, і трави, і води...
В годину щасливу і в радості мить,
любіть у годину негоди.
Любіть Україну у сні й наяву,
вишневу свою Україну,
красу її, вічно живу і нову,
і мову її солов'їну.
Без неї — ніщо ми, як порох і дим,
розвіяний в полі вітрами...
Любіть Україну всім серцем своїм
і всіми своїми ділами."""

styled_header = text_style(header, 'bold')
styled_header = text_color(styled_header, 'black')
styled_header = background_color(styled_header, 'purple')

styled_text = text_style(text, 'italic')
styled_text = text_color(styled_text, 'black')
styled_text = background_color(styled_text, 'purple')

print(styled_header)
print(styled_text)
