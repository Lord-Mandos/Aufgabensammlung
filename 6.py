text = "Am Freitag gibt es viel Sonnenschein und nur lockere Wolken. Im Süden ist es etwas wolkiger und zu den Alpen hin sind lokale Schauer möglich. 14 bis 25 Grad. Am Samstag ist es trocken und verbreitet sonnig mit lockeren Quellwolken. Nur an den Alpen entwickeln sich aus dickeren Quellwolken einzelne Schauer. 15 bis 25 Grad. Am Sonntag ziehen von Norden her im Tagesverlauf dichtere Wolkenfelder auf, aber nur selten fallen ein paar Regentropfen. In der Südhälfte ist es sonnig und trocken, nur zu den Alpen hin gibt es dickere Quellwolken mit einzelnen Schauern und Gewittern. 16 bis 27 Grad."
clean_text = ""

# Schleife, um Sonderzeichen zu entfernen und eine bereinigte Version des Textes zu erstellen
for letter in text:
    if letter.isalnum() or letter.isspace():    
        
        clean_text += letter

words = clean_text.split()      #teile text in wörter Erstellt liste

longest_word = [words[0]]       #initialisiere start liste mit erstem Wort


for word in words:                          #durchlaufe jedes wort
    if (len(word) > len(longest_word[0])):    #->prüfe ob länger
        longest_word = [word]                 #-->erstzte liste
    elif (len(word) == len(longest_word[0])): #->prüfe ob gleich lang
        longest_word.append(word)             #-->füge zu liste hinzu


print(longest_word)