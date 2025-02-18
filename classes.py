import random

class Uczen:
    def __init__(self, imie, nazwisko, punkty):
        self.id = id(self)
        self.imie = imie
        self.nazwisko = nazwisko
        self.plec = random.choice(["M", "F"])
        self.punkty = punkty

    def dodajPunkty(self, punkty):
        self.punkty += punkty

    def zaryczNo(self):
        print(f"ID: {self.id}, Imię: {self.imie}, Nazwisko: {self.nazwisko}, Płeć: {self.plec}, Punkty: {self.punkty}")

    def __int__(self):
        return self.punkty

    def __str__(self):
        return f"ID: {self.id}, Imię: {self.imie}, Nazwisko: {self.nazwisko}, Płeć: {self.plec}, Punkty: {self.punkty}"


class Klasa:
    def __init__(self, nazwa, wychowawca):
        self.lista_uczniow = []
        self.nazwa = nazwa
        self.id = id(self)
        self.srednia_punktow = 0
        self.wychowawca = wychowawca
        self.imiona_uczniow = []
        self.nazwiska_uczniow = []

    def zbiorka(self):
        for imie, nazwisko in zip(self.imiona_uczniow, self.nazwiska_uczniow):
            print(f"Imię: {imie}, Nazwisko: {nazwisko}")

    def dodajUcznia(self, uczen):
        self.lista_uczniow.append(uczen)
        self.imiona_uczniow.append(uczen.imie)
        self.nazwiska_uczniow.append(uczen.nazwisko)
        self.srednia_punktow = sum(uczen.punkty for uczen in self.lista_uczniow) / len(self.lista_uczniow)


class Szkola:
    def __init__(self, nazwa):
        self.lista_klas = []
        self.nazwa = nazwa
        self.id = id(self)

    def srednia_punktacja(self):
        srednia = sum(klasa.srednia_punktow for klasa in self.lista_klas) / len(self.lista_klas)
        print(f"Średnia punktacja w szkole: {srednia}")

    def ilosc_uczniow(self):
        liczba_uczniow = sum(len(klasa.lista_uczniow) for klasa in self.lista_klas)
        print(f"Ilość uczniów w szkole: {liczba_uczniow}")

    def wypisz(self):
        for klasa in self.lista_klas:
            print(f"Klasa {klasa.nazwa}:")
            klasa.zbiorka()

    def dodajKlase(self, klasa):
        self.lista_klas.append(klasa)

    def dodajUcznia(self, uczen):
        random_klasa = random.choice(self.lista_klas)
        random_klasa.dodajUcznia(uczen)


# Przykład użycia:

ucz1 = Uczen("Jan", "Kowalski", 80)
ucz2 = Uczen("Anna", "Nowak", 90)
ucz3 = Uczen("Piotr", "Czerwony", 75)

klasaA = Klasa("A", "Pan Smith")
klasaB = Klasa("B", "Pani Johnson")

szkola = Szkola("Szkoła Podstawowa Nr 1")

klasaA.dodajUcznia(ucz1)
klasaB.dodajUcznia(ucz2)
klasaB.dodajUcznia(ucz3)

szkola.dodajKlase(klasaA)
szkola.dodajKlase(klasaB)

szkola.wypisz()
szkola.srednia_punktacja()
szkola.ilosc_uczniow()
