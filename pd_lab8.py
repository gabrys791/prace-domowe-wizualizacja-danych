import pandas as pd
import numpy as np
#zad1
# data=pd.read_excel('imiona.xlsx')
# df=pd.DataFrame(data)
# print(df)
#zad2
# print(df[df['Liczba']<1000])
# print(df[df['Imie']=='GABRIEL'])
# print(df['Liczba'].sum())
# print((df[(df['Rok']>2000) & (df['Rok']<2005)].sum()))
# zad2_5=df.groupby('Plec').sum()
# print(zad2_5)


#zad3
df2 = pd.read_csv('zamowienia.csv',header=0,sep=';',decimal='.')
print(df2)

unik = df2['Sprzedawca'].unique()
print(unik)
print(df2.sort_values('Utarg', ascending = False).head(5))

print(df2.groupby(['Sprzedawca']).size().reset_index(name='ile'))

print(df2.groupby(['Kraj'])[["Utarg"]].sum())
df2['Data zamowienia'] = pd.to_datetime(df2['Data zamowienia'])
print(df2[((df2['Kraj']=='Polska') & (pd.DatetimeIndex(df2['Data zamowienia']).year == 2005))].agg({'Utarg':['sum']}))

print(df2[(pd.DatetimeIndex(df2['Data zamowienia']).year == 2004)]['Utarg'].mean(axis=0))

df3=df2[(pd.DatetimeIndex(df2['Data zamowienia']).year == 2004)]

df4=df2[(pd.DatetimeIndex(df2['Data zamowienia']).year == 2005)]

df3.to_csv('zamówienia_2004.csv',index=False)

df4.to_csv('zamówienia_2005.csv',index=False)

