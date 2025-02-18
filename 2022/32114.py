blokow = int(input("Wprowadź liczbę bloków: "))

wysokosc = 0
w_warstwie = 1
while w_warstwie <= blokow:
    wysokosc += 1
    blokow -= w_warstwie
    w_warstwie += 1

print("Wysokość piramidy wynosi:", wysokosc)
