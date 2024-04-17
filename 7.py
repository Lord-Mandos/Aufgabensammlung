text = "Am Freitag gibt es viel Sonnenschein und nur lockere Wolken. Im Süden ist es etwas wolkiger und zu den Alpen hin sind lokale Schauer möglich. 14 bis 25 Grad. Am Samstag ist es trocken und verbreitet sonnig mit lockeren Quellwolken. Nur an den Alpen entwickeln sich aus dickeren Quellwolken einzelne Schauer. 15 bis 25 Grad. Am Sonntag ziehen von Norden her im Tagesverlauf dichtere Wolkenfelder auf, aber nur selten fallen ein paar Regentropfen. In der Südhälfte ist es sonnig und trocken, nur zu den Alpen hin gibt es dickere Quellwolken mit einzelnen Schauern und Gewittern. 16 bis 27 Grad."

split_text = text.split()

clear_text = ""

for word in split_text:

    
    if word[-1] == "." :
        clear_text += word + "\n"
    else:
        clear_text += word + " "
    
print(clear_text)