text = "Victor jagt zwölf Boxkämpfer quer über den großen Üsterer Deich."
clean_text = ""
for item in text:
    if item.lower() == "ä":
        clean_text += "ae" if item.islower() else "Ae"
        
    elif item.lower() == "ö":
        clean_text += "oe" if item.islower() else "Oe"
        
    elif item.lower() == "ü":
        clean_text += "ue" if item.islower() else "Ue"

    else:
        clean_text += item

print(clean_text)