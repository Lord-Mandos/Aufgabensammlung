text = "Heute ist ein toller Tag! #Sonnenschein ☀️ und gute Laune! 😊 #Freitag"
clean_text=""

if not text:
    print("!! Fehler !!\n Kein Text")

for item in text:
    if item.isalnum():
        clean_text += item

print(clean_text)