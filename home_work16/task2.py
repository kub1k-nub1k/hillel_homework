def longest_words(file):
    with open(file, 'r',  encoding="utf-8") as f:
        words = f.read().split()

        max_length = max(len(word) for word in words)

        long_words = [word for word in words if len(word) == max_length]

        if len(long_words) == 1:
            print("Слово з максимальною довжиною:", long_words[0])
        else:
            print("Слова з максимальною довжиною:", ", ".join(long_words))


longest_words("article.txt")
