word = input("Gib mir dein Wort!!")
word = word.strip()
word_length = len(word)

if word_length % 2 == 0:
    word_length = word_length // 2
    print(f"{word[word_length - 1]} {word[word_length]}")
else:
    print(f"{word[word_length // 2]}")