import math
def calka(f,xo,xn,n):
    h = (xn - xo) / n
    res = 0
    x = xo + (h / 2)
    for x in range(n):
        res += x
        x += h
    return h * res
print(calka(math.sin(4),0,100,10))