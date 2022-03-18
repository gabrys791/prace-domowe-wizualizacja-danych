#zad1
# import random
# lista=[]
# for i in range(0,10):
#     a=random.randint(0,30)
#     lista.append(a*2)
# print(lista)
# plik=open('liczby.txt','w+')
# plik.writelines(str(lista))

#zad2
# plik=open('liczby.txt','r')
# linia=plik.readline()
# plik.close()
# print(linia)
#zad3
# with open('text.txt','r+') as plik:
#     for i in range(0,5):
#         plik.write('hej ')
# plik=open('text.txt','r')
# znaki=plik.readline()
# print(znaki)
#zad4
# class Na_zakupy:
#     def __init__(self,nazwa,ilosc,jednostka,cena_jd):
#         self.nazwa=nazwa
#         self.ilosc=ilosc
#         self.jednostka=jednostka
#         self.cena_jd=cena_jd
#     def	wyświetl_produkt(self):
#         print(self.nazwa)
#     def ile_produktu(self):
#         print(self.nazwa+' '+self.ilosc+' '+self.jednostka)
#     def cena(self):
#         print(self.cena*self.cena_jd)
#zad5
# class ciag:
#     def __init__(self, a1,r,n):
#         self.a1=a1
#         self.r=r
#         self.n=n
#         self.ciag = [a1 +r * x for x in range(0,n)]
#     def wyswietl(self):
#         print(self.a1,'',self.r,'',self.n)
#     def policz_sume(self):
#         suma=0
#
#         for x in range(0,self.n):
#             suma+=self.ciag[x]
#         return suma
#     def policz_element(self):
#         self.an=self.a1+self.r*(self.n-1)
#         return self.an
#
# jakis=ciag(2,2,8)
#
# print(jakis.policz_element())
# print(jakis.policz_sume())
# print(jakis.wyswietl())
#zad6
class Robaczek:
    def __init__(self,x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok
    def dogory(self,ile):
        self.y = self.y + self.krok*ile
        return self.y
    def nadol(self,ile):
        self.y=self.y - self.krok
        return self.y
    def wlewo(self,ile):
        self.x=self.x - self.krok*ile
        return self.x
    def wprawo(self,ile):
        self.x=self.x + self.krok*ile
        return self.x
    def gdziejestem(self):
        print(self.x,self.y)

robal=Robaczek(0,0,1)
print(robal.gdziejestem())
print(robal.dogory(2))
print(robal.gdziejestem())
print(robal.dogory(1))
print(robal.gdziejestem())
print(robal.wlewo(1))
print(robal.gdziejestem())
print(robal.wprawo(1))
print(robal.gdziejestem())
print(robal.nadol(1))
print(robal.gdziejestem())
print(robal.wlewo(1))
print(robal.gdziejestem())











