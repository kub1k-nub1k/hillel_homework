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

sort_text = text.replace(",", "").replace(".", "").replace("\n", " ").lower()

words = sort_text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

most_word = max(word_count, key=word_count.get)
most_count = word_count[most_word]

print(f"Найпоширеніше слово: '{most_word}', кількість входжень: {most_count}")

least_word = min(word_count, key=word_count.get)
least_count = word_count[least_word]

print(f"Найменше поширене слово: '{least_word}', кількість входжень: {least_count}")
