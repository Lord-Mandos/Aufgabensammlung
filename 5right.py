text = "Python is my passion my."
text_length = len(text)

search = input("Welches Wort wird gesucht?")

counter = 0
position = 1
found = False


while text_length > counter:
    
    position = text.lower().find(search.lower(), counter)
    #Sollte das Wort nicht da sein ist position -1 und die Schleife bricht ab
    if position < 0:
        break
    else:
        found = True
        position += len(search)
        print(f"{search} an Position {position}")
        counter += position

if found == True:
    print("Keine weiteren Uebereinstimmungen gefunden")
else:
    print("Keine Uebereinstimmung endeckt")