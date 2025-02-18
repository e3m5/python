from abc import ABC

from organizm import Organizm
import random




class Roslina(Organizm, ABC):
    max_roslin = 45

    def akcja(self):
        if self._swiat.liczba_roslin() < self.max_roslin:
            if random.random() < 0.1:  # Mała szansa na rozsiew
                nowe_x, nowe_y = self._losuj_sasiednie_pole()  # Wywołanie poprawnej metody
                if self._swiat.sprawdz_kolizje(nowe_x, nowe_y) is None:
                    self._swiat.dodaj_organizm(self.__class__((nowe_x, nowe_y), self._swiat))

    def kolizja(self, zwierze):
            if self.__class__.__name__ == "Guarana":
                zwierze.sila += 3
                self._swiat.usun_organizm(self)
            elif self.__class__.__name__ == "WilczeJagody":
                self._swiat.usun_organizm(zwierze)
                self._swiat.usun_organizm(self)
