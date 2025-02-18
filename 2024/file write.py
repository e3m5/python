#4.1
with open("konta.txt", "r") as f:
    pseudonimy = set()
    for line in f:
        pseudonimA, pseudonimB = line.strip().split()
        pseudonimy.add(pseudonimA)
        pseudonimy.add(pseudonimB)
    print(len(pseudonimy))

#4.2

with open("konta.txt", "r") as f:
    konta = set()
    for line in f:
        pseudonimA, pseudonimB = line.strip().split()
        konta.add(pseudonimA)
        konta.add(pseudonimB)

    falszywe_konta = set()
    for konto in konta:
        if konta.count(konto) == 1:
            falszywe_konta.add(konto)
    print(falszywe_konta)

#4.3
with open("konta.txt", "r") as f:
    konta = set()
    for line in f:
        pseudonimA, pseudonimB = line.strip().split()
        konta.add((pseudonimA, pseudonimB))
        konta.add((pseudonimB, pseudonimA))
    nawzajem = 0
    for para in konta:
        if konta.count(para) == 2:
            nawzajem += 1
    print(nawzajem)

#4.4
with open("konta.txt", "r") as f:
    konta = {}
    for line in f:
        pseudonimA, pseudonimB = line.strip().split()
        if pseudonimA not in konta:
            konta[pseudonimA] = 0
        if pseudonimB not in konta:
            konta[pseudonimB] = 0
        konta[pseudonimA] += 1
        konta[pseudonimB] += 1
    najwiecej_obserwujacy = max(konta, key=konta.get)
    print(najwiecej_obserwujacy)