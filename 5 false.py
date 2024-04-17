text = "Python is my passion."
words = text.split()
search = input("Welches Wort wird gesucht?")
counter = 0

print(words)
if search in words:
    print(f"{search} gefunden an stelle {words.index(search) + 1}")