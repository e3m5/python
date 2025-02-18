#1
import datetime
print('podaj imie\n')
x = input()
if not x.endswith('a')  or x.lower() == 'kuba':
    print("imie jest męskie")
else:    
    print("imie nie jest męskie")
wielka_litera = x.replace(x,x[0],1)
print(wielka_litera.capitalize())
from datetime import date
dzis = date(2023,9,13)
koniec = date(2024,6,21)
roznica= koniec - dzis
print(roznica.days)