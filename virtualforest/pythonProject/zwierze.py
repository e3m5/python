from abc import ABC

from organizm import Organizm
import random


class Zwierze(Organizm, ABC):
    def akcja(self):
        dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        nowe_x = (self._polozenie[0] + dx) % self._swiat.n
        nowe_y = (self._polozenie[1] + dy) % self._swiat.n
        if self._swiat.sprawdz_kolizje(nowe_x, nowe_y) is None:
            self._polozenie = (nowe_x, nowe_y)

    def kolizja(self, zwierze):
        if isinstance(zwierze ,self.__class__):
            # rozmnażanie
            nowe_x, nowe_y = self._losuj_sasiednie_pole()
            if self._swiat.sprawdz_kolizje(nowe_x, nowe_y) is None:
                self._swiat.dodaj_organizm(self.__class__((nowe_x, nowe_y), self._swiat()))
        else:
            # walka
            if self._sila >= zwierze.sila:
                self._swiat.usun_organizm(zwierze)
            else:
                self._swiat.usun_organizm(self)

    def _losuj_sasiednie_pole(self):
        dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        nowe_x = (self._polozenie[0] + dx) % self._swiat.n
        nowe_y = (self._polozenie[1] + dy) % self._swiat.n
        return nowe_x, nowe_y
