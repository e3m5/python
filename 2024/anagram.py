def czy_anagram(slowo1, slowo2):
    x = [slowo1[i] for i in range(0,len(slowo1))]
    x.sort()
    y = [slowo2[i] for i in range(0,len(slowo2))]
    y.sort()
    if (x==y): return True
    else:
         return False
print (czy_anagram('kot','pies'))

def czy_palindrom(slowo):
    slowo = slowo.lower()
    dl = len(slowo)
    if dl < 2 : return True
    elif slowo[0] == slowo[dl - 1]: return czy_palindrom(slowo[1: dl - 1])
    
    else:
        return False 
print (czy_palindrom('Kajak'))
