slowo_uzytkownika = input("Wprowadź słowo do zjedzenia samogłosek: ")
slowo_uzytkownika = slowo_uzytkownika.upper()

for litera in slowo_uzytkownika:
    if litera == "A":
        continue
    elif litera == "E":
        continue
    elif litera == "I":
        continue
    elif litera == "O":
        continue
    elif litera == "U":
        continue
    else:
        print(litera)