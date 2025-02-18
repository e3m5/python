slowo_bez_samoglosek = ""

slowo_uzytkownika = input("Wprowadź słowo: ")
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
        slowo_bez_samoglosek += litera
		
print(slowo_bez_samoglosek)
