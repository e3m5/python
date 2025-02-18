from zwierze import Zwierze
import pygame
import random

class Wilk(Zwierze):
    def __init__(self, polozenie, swiat):
        super().__init__(sila=9, inicjatywa=5, polozenie=polozenie, swiat=swiat)

    def rysowanie(self, screen):
        pygame.draw.circle(screen, (128, 128, 128), (self.polozenie[0] * 20, self.polozenie[1] * 20), 10)


class Owca(Zwierze):
    def __init__(self, polozenie, swiat):
        super().__init__(sila=4, inicjatywa=4, polozenie=polozenie, swiat=swiat)

    def rysowanie(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.polozenie[0] * 20, self.polozenie[1] * 20), 8)


class Byk(Zwierze):
    def __init__(self, polozenie, swiat):
        super().__init__(sila=10, inicjatywa=7, polozenie=polozenie, swiat=swiat)

    def akcja(self):
        if random.random() < 0.09:
            super().akcja()

    def kolizja(self, zwierze):
        if zwierze.sila < 9:
            return
        if zwierze.sila < 5:
            return
        super().kolizja(zwierze)

    def rysowanie(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.polozenie[0] * 20, self.polozenie[1] * 20), 10)


class Zmija(Zwierze):
    def __init__(self, polozenie, swiat):
        super().__init__(sila=2, inicjatywa=3, polozenie=polozenie, swiat=swiat)

    def kolizja(self, zwierze):
        if self.sila < zwierze.sila:
            self._swiat.usun_organizm(self)
            self._swiat.usun_organizm(zwierze)
        else:
            super().kolizja(zwierze)

    def rysowanie(self, screen):
        pygame.draw.circle(screen, (0, 128, 0), (self.polozenie[0] * 20, self.polozenie[1] * 20), 6)


class Lew(Zwierze):
    def __init__(self, polozenie, swiat):
        super().__init__(sila=11, inicjatywa=7, polozenie=polozenie, swiat=swiat)

    def kolizja(self, zwierze):
        if zwierze.sila < 5:
            return
        super().kolizja(zwierze)

    def rysowanie(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (self.polozenie[0] * 20, self.polozenie[1] * 20), 15)
