text = "Heute ist ein toller Tag! #Sonnenschein ☀️ und gute Laune! 😊 #Freitag"
counter = 1

if not text:
    print("!! Fehler !!\n Kein Text")
    counter = 0

for item in text.strip():
    if item == " ":
        counter += 1

print(counter)