import pygame
from swiat import Swiat
from rosliny import Trawa, Guarana, WilczeJagody
from zwierzeta import Wilk, Owca, Byk, Zmija, Lew

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Symulator Świata")

    swiat = Swiat(40)

    swiat.dodaj_organizm(Wilk((5, 5), swiat))
    swiat.dodaj_organizm(Owca((10, 10), swiat))
    swiat.dodaj_organizm(Owca((14, 10), swiat))
    swiat.dodaj_organizm(Owca((20, 10), swiat))
    swiat.dodaj_organizm(Byk((15, 15), swiat))
    swiat.dodaj_organizm(Zmija((12, 12), swiat))
    swiat.dodaj_organizm(Lew((4, 4), swiat))
    swiat.dodaj_organizm(Trawa((8, 8), swiat))
    swiat.dodaj_organizm(Guarana((14, 14), swiat))
    swiat.dodaj_organizm(WilczeJagody((6, 6), swiat))

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((136, 218, 63))  # Kolor tła (zielony)
        swiat.rysuj_swiat(screen)     # Rysowanie świata
        pygame.display.flip()         # Aktualizacja ekranu

        swiat.wykonaj_ture()           # Przebieg tury
        clock.tick(1)                  # Zwolnienie na 1 FPS dla obserwacji tur

    pygame.quit()

if __name__ == "__main__":
    main()
