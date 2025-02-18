from roslina import Roslina
import pygame

class Trawa(Roslina):
    max_roslin = 30
    def __init__(self, polozenie, swiat):
        super().__init__(sila=0, inicjatywa=0, polozenie=polozenie, swiat=swiat)

    def rysowanie(self, screen):
        # Rysowanie trawy (zielone kółko)
        pygame.draw.circle(screen, (0, 255, 0), (self.polozenie[0] * 20, self.polozenie[1] * 20), 5)


class Guarana(Roslina):
    max_roslin = 10
    def __init__(self, polozenie, swiat):
        super().__init__(sila=0, inicjatywa=0, polozenie=polozenie, swiat=swiat)

    def kolizja(self, zwierze):
        # Zwiększenie siły zwierzęcia o 3
        zwierze.sila += 3
        self._swiat.usun_organizm(self)

    def rysowanie(self, screen):
        # Rysowanie guarany (niebieskie kółko)
        pygame.draw.circle(screen, (0, 0, 255), (self.polozenie[0] * 20, self.polozenie[1] * 20), 5)


class WilczeJagody(Roslina):
    max_roslin = 5
    def __init__(self, polozenie, swiat):
        super().__init__(sila=0, inicjatywa=0, polozenie=polozenie, swiat=swiat)

    def kolizja(self, zwierze):
        # Zwierzę, które zje wilcze jagody, ginie
        self._swiat.usun_organizm(zwierze)
        self._swiat.usun_organizm(self)

    def rysowanie(self, screen):
        # Rysowanie wilczych jagód (fioletowe kółko)
        pygame.draw.circle(screen, (128, 0, 128), (self.polozenie[0] * 20, self.polozenie[1] * 20), 5)
