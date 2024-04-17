text = "Ich kann mit mehreren Worten eine Variabel beschreiben"

words = text.lower().split()
camel_text = ""

for word in words:
    camel_text += word.capitalize()

camel_text = camel_text[0].lower() + camel_text[1:]

print(camel_text)


############### Title version ###############

text = text.title().replace( " ", "")
text = text[0].lower() + text[1:]
print(text)