text = "Ich kann mit mehreren Worten eine Variabel beschreiben"

words = text.lower().split()

camel_text = ""
first = True

for word in words:
    if first == True:
        camel_text += word
        first = False
    else:
        camel_text += word[0].upper()
        camel_text += word[1:]

print(camel_text)