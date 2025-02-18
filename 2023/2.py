#input slowo/litera/liczba
#output:czy slowo jest palindromem,czy litera znajduje sie w slowie
#czy liczba liter w slowie x2 > liczba?
slowo = input('podaj słowo:\n')
litera = input('podaj wybraną literę:\n')
liczba = int(input('podaj wybraną liczbę:\n'))
if slowo[0] == slowo[-1]:
    print('słowo jest palindromem')
else:
    print('słowo nie jest palindromem')
if litera.lower() in slowo:
    print( 'litera znajduje się w podanym wyrazie')
else:
    print('litera nie znajduje sie w podanym wyrazie')
liczbaliter = len(slowo) * 2
if liczbaliter > liczba:
    print('podwojona długość słowa jest wieksza od podanej liczby')
else:
    print('podwojona długość słowa nie jest wieksza od podanej liczby')
