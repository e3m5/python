def enigma():
   
    rotor1 = "MDUYRCBJPLQNAWZOTVFIEKSXHG"
    rotor2 = "SJLHQRIWNXTGZPOAMFUBCKDEYV"
    rotor3 = "RCAVKYXSIGBZEDWMTFNLUQHJOP"
    baza = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    rotory = [rotor1, rotor2, rotor3]
    plugboard = "AV BH LE GI MS EJ QP PC VO MD SR"
    ustawienie1 = 0
    ustawienie2 = 0
    ustawienie3 = 0
    kroki = [19,3,4]
    reflektor="GJLHPVTOQNYCKFDUSMRIAWXBZE"
    
    wiadomosc = str(input("podaj zdanie: ")).upper()
    szyfr = " "
       