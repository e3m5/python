def funkcja0(a,b,c,d):
    lista = [a,b,c,d]
    najmniejszaliczba = lista[0]
    for i in range(1,len(lista)):
        if lista[i] < najmniejszaliczba:
            najmniejszaliczba = lista[i]
    print(i)
funkcja0(8,3,2,5)   

def funkcja1(a,b,c,d,e,f):
    lista = [a,b,c,d,e,f]
    for i in range(0, len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] >= lista[j]:
                lista[i], lista[j] = lista[j],lista[i]
    print(lista)
funkcja1(4,2,2,5,1,12)

def funkcja2(a,b):
    norma = (a**2 + b**2)**(1/2)
    print(norma)
funkcja2(3,4)

def fcja3(a,b,c):
    avg = (a+b+c)/3
    odchstd = (int(((a-avg)**2+(b-avg)**2+(c-avg)**2)/3)**(1/2))
    print(odchstd)
fcja3(1,2,3)

def fcja4(a,b,c,d,e,f):
    lista=[a,b,c,d,e,f]
    odwrot = lista[::-1]
    print(odwrot)
fcja4(4,2,2,5,1,12)