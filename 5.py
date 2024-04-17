text = "Python is my passion."

#Text in einzel wörter aufteilen
words = text.split()
search = input("Welches Wort wird gesucht?")
counter = 0
found = False

for word in words:
    if word.lower() == search.lower():
        counter += len(word)
        found = True
        break
    else:
        #Länge des Wortes zum counter aufzählen
        counter += len(word) + 1

if found == True:
    print(f"{search} wurde an stelle {counter} gefunden.")
else:
    print(f"{search} kann nicht gefunden werden.")