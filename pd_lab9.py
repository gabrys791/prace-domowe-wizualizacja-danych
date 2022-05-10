import pandas as pd
import matplotlib.pyplot as plt
#zad1
# data=pd.read_excel('imiona.xlsx')
# df=pd.DataFrame(data)
# grupa=df.groupby('Rok').agg({'Liczba':['sum']})
# print(grupa)
# grupa.plot(xlabel='Rok',ylabel='Liczba Dzieci',rot=0,title='Liczba dzieci urodzonych w poszczególnych latach')
# plt.show()
#zad2
# grupa=df.groupby('Plec').agg({'Liczba':['sum']})
# wykres=grupa.plot.bar()
# wykres.set_xlabel('Płeć')
# wykres.set_ylabel('liczba dzieci w mld')
# wykres.legend()
# plt.show()
#zad3
# grupa=(df[(df['Rok']>2012)&(df['Rok']<2017)].groupby('Plec').agg({'Liczba':['sum']}))
# grupa.plot.pie(subplots=True,autopct='%.2f%%',fontsize=20,figsize=(6,6))
# plt.show()
#zad4
data=pd.read_csv('zamowienia.csv',sep=';',decimal=':')
df=pd.DataFrame(data)
print(df)
grupa=df.groupby('Sprzedawca').agg({'idZamowienia':['count']})
#grupa.plot(xlabel='Sprzedawca',ylabel='Liczba zamowien',rot=0,title='liczba zamowien sprzedawców')
wykres=grupa.plot.bar()
wykres.set_xlabel('sprzedawca')
wykres.set_ylabel('liczba zamowien')
wykres.legend()
plt.show()

print(grupa)