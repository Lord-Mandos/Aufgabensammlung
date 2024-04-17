text = "Python ist wie Englisch sprechen, nur ohne Zeichensetzung und dass man es schreibt"
vowels = "aeiou"
clean_text = ""

for item in text:

    if item.lower() not in vowels:
        clean_text += item

print(clean_text)