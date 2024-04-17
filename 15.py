phone_number = input("Gib mir deine nummer(Nur zahlen (0-9)):")
phone_number = phone_number.strip()

if phone_number.isdigit():
    if len(phone_number) == 18 and phone_number.startswith("00"):
        print(f"(+{phone_number[2:4]}) {phone_number[4:8]} {phone_number[8:11]} - {phone_number[11:14]} {phone_number[14:17]} {phone_number[17]}")
    elif len(phone_number) == 15:
        print(f"({phone_number[0:5]}) {phone_number[5:8]} - {phone_number[8:11]} {phone_number[11:14]} {phone_number[14]}")
else:
    print("!! Fehler !! \nPrüfe die Eingabe deiner Nummer")

#   004912345678965431
#   012345678965431