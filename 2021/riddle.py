tajny_numer = 777

print(
"""
+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
""")

liczba_uzytkownika = int(input("Wprowadź liczbę: "))

while liczba_uzytkownika != tajny_numer:
    print("Ha ha! Utknąłeś w mojej pętli!")
    liczba_uzytkownika = int(input("Wprowadź liczbę jeszcze raz: "))
print(tajny_numer, "Dobra robota, mugolu! Jesteś teraz wolny.")
