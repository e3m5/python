from roslina import Roslina


class Swiat:
    def __init__(self, n=40):
        self.n = n #rozmiar planszy
        self.organizmy = [] #lista instancji organizmow
        self.tura = 0


    def dodaj_organizm(self, organizm):
        self.organizmy.append(organizm)

    def liczba_roslin(self): #zliczanie roslin w symulacji
        return sum(1 for organizm in self.organizmy if isinstance(organizm, Roslina))

    def wykonaj_ture(self):
        # Sortowanie po inicjatywie i wieku
        self.organizmy.sort(key=lambda o: (-o.inicjatywa, -o.wiek)) #klucz sortowania malejacego
        for organizm in self.organizmy:
            organizm.akcja()
            organizm.starzej_sie()
        self.tura += 1

    def rysuj_swiat(self, screen):
        for organizm in self.organizmy:
            organizm.rysowanie(screen)

    def usun_organizm(self, organizm):
        if organizm in self.organizmy:
            self.organizmy.remove(organizm)

    def sprawdz_kolizje(self, x, y):
        # sprawdzanie kolizji na danym polu
        organizmy_na_polu = [o for o in self.organizmy if o.polozenie == (x, y)]
        if len(organizmy_na_polu) > 1: #wiecej niz 1 organizm stoi na owym polu
            for i in range(1, len(organizmy_na_polu)):
                organizmy_na_polu[0].kolizja(organizmy_na_polu[i])
