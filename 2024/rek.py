#def nwd(a,b):
 #   if a == 0: return b
##   return nwd(b%a, a)
#a = 7
#b = 40
#print(nwd(a,b))

def algorytm(n):
    if n <= 1:
       return n
    else: return(algorytm(n-1) + algorytm(n-2))
wyrazy = 5
if wyrazy <= 0:
   print("blad")
else:
   print("ciąg:")
   for i in range(wyrazy):
       print(algorytm(i))

print("                             ")
print("-|-|-|-|-|-|-|-|-|-|-|-|-|-|-")
print("                             ")

def rozklad(n):
    czynniki = []
    dwa = 2
    while n != 1:
        while n % dwa == 0:
            n //= dwa
            czynniki.append(dwa)
        dwa += 1
    
    return czynniki
print(rozklad(90))