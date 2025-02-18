from abc import ABC, abstractmethod
import random


class Organizm(ABC):
    def __init__(self, sila, inicjatywa, polozenie, swiat):
        self._sila = sila
        self._inicjatywa = inicjatywa
        self._polozenie = polozenie
        self._swiat = swiat
        self._wiek = 0

    @property
    def sila(self):
        return self._sila

    @property
    def inicjatywa(self):
        return self._inicjatywa

    @property
    def polozenie(self):
        return self._polozenie

    @abstractmethod
    def akcja(self):
        pass

    @abstractmethod
    def kolizja(self, organizm):
        pass

    @abstractmethod
    def rysowanie(self, screen):
        pass


    @property
    def wiek(self):
        return self._wiek

    def starzej_sie(self):
        self._wiek += 1

    def _losuj_sasiednie_pole(self):
        x, y = self._polozenie
        dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])  # ruch 4 kierunkowy
        nowe_x = (x + dx) % self._swiat.n
        nowe_y = (y + dy) % self._swiat.n
        return nowe_x, nowe_y