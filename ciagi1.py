def suma_arytmetyczna(a1,an,n):
    Sn=((a1+an)*n)/2
    return Sn
def wyraz_arytmetyczny(a1,n,r):
    an=a1+(n-1)*r
    return an
def suma_geometryczna(a1,q,n):
    if q!=1:
     Sn=a1*(1-q**n)/(1-q)
    else:
        Sn=a1*n
    return Sn
def wyraz_geometryczny(a1,q,n):
    an=a1*q**(n-1)
    return an