phone_number = input("Gib mir deine 15 Stellige nummer:")

if len(phone_number) == 15:
    print(f"({phone_number[0:5]}) {phone_number[5:8]} - {phone_number[8:11]} {phone_number[11:14]} {phone_number[14]}")
else:
    print("Fehler prüfe auf korrekte eingabe")

