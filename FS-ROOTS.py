from math import cos, sin, pi
from random import uniform
# This Function Takes an array that contains Coefficients of the Polynomial
def FindRoots(coef):
    N=len(coef)-1
#---------------------------------------------------------------------------------------------
    P = lambda x: sum(coef*(pow(x, i)) for i, coef in enumerate(coef))
    dp = lambda x: sum(i*coef*(pow(x, i-1)) for i, coef in enumerate(coef)) 
#-----------------------------------------------------------------------------------------------------------------------------------------------
    U = 1 + 1 / abs(coef[-1]) * max(list(map(abs,coef)))
    V = abs(coef[0]) / (abs(coef[0]) + max(list(map(abs,coef))))      
    def Roots0(f):
        r = uniform(V, U)
        a = uniform(0, pi*2)
        return complex(r * cos(a), r * sin(a))           
    roots = list(map(Roots0, range(N)))
    NP=0
    inn=0
    while NP<N:
        inn=inn+1
        NP = 0
        for k, r in enumerate(roots):
            ratio =  P(r) / dp(r)
            w = ratio / (1 - (ratio * sum(1/(r - x) 
                              for j, x in enumerate(roots) if j != k)))
            if round(w.real,2) == 0 and round(w.imag, 2) == 0:
                NP += 1
            roots[k] -= w
    print(inn)
    return list(map(lambda r:complex(round(r.real, 16), round(r.imag, 16)), roots))  

