#zad1
# lista=[1-x for x in range(1,10)]
# print(lista)
# lista2=[4**x for x in range(0,10)]
# print(lista2)
# lista3=[x for x in range(0,10) if x%2==0]
# print(lista3)
#zad2
# import random
# lista=[]
# for x in range(0,10):
#     lista.append(random.randint(0,10))
# print(lista)
# lista2=[x for x in lista if x%2==0]
# print(lista2)
#zad3
# slownik={"jajka":"3szt","mleko":"2litry","bulki":"6szt","sok":"2litry"}
#
# slownik2={value:key for key ,value in slownik.items()}
# print(slownik2)
#zad4
# def czyprostokatny(a,b,c):
#     if a**2+b**2==c**2:
#         return "tak"
#     else:
#         return "nie"
# print(czyprostokatny(3,4,5))
# print(czyprostokatny(1,2,3))
#zad5
# def poletrapezu(a=0,b=0,h=0):
#     pole=((a+b)*h)/2
#     return pole
#
# print(poletrapezu())
# print(poletrapezu(1,2,3))
#zad6
# def elementyciagu(a=1,b=4,ile=10):
#     for x in range(0,ile):
#         a=a*b
#     return a
# print(elementyciagu())
#zad7
# def elementyciagu(*liczby):
#     if liczby==0:
#         return 0
#     else:
#      suma=1
#     for x in liczby:
#         suma*=x
#     return suma
#
# print(elementyciagu(4,4,4,4,4,4,4,4,4,4))
#zad8

# def lista_zakupow(**rzeczy):
#         ilosc=0
#         laczna_cena=0
#         for cena in rzeczy:
#                 ilosc+=1
#                 laczna_cena+=rzeczy[cena]
#         print(ilosc)
#         print(laczna_cena)
#
#
#
# lista_zakupow(mleko=2,chleb=1.10,ziemniaki=2,maslo=7.50,sok=4.30)

#zad9
import ciagi1
print(ciagi1.suma_arytmetyczna(1,3,3))
print(ciagi1.suma_geometryczna(1,2,4))
print(ciagi1.wyraz_arytmetyczny(3,4,2))
print(ciagi1.wyraz_geometryczny(3,3,4))








