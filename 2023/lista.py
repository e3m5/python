#input liczba n
#lista o wielkosci n,jesli n > 10 to do listy generujemy losowo n liczb z zakresu -1000;1000,inaczej uzytkownik wpisuje je recznie
#output suma liczb i ich srednia,iloczyn pierwszego i ostatniego elementu
#wypisanie liczb od konca w osobnych linijkach
#najmniejsza i najwieksza liczba (różnica)
#sprawdzenie czy liczba jest ujmna
import random
liczbaN=int(input("podaj długosc listy:\n"))
if liczbaN > 10:
    lista = [random.randrange(-1000, 1000, 3) for i in range(liczbaN)]
else:
    lista = []
    listdlugosc = liczbaN 
    for idx in range(listdlugosc):
        liczby = int(input("podaj tyle samo liczb ile lista ma miec dlugosci:\n"))
        lista.append(liczby)
result = 0
for num in lista:
    result += num
print("suma liczb:" , result)

if result < 0:
    print("liczba jest ujemna")

for i in lista[::-1]:
    print(i)