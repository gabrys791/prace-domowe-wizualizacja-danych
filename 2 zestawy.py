import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
# plt.subplots(2,1)
# plt.subplot(1,2,1)
# plt.barh(['A','B','C','D','E'],[35,45,15,41,40],color=['powderblue','pink','coral','grey','purple'])
# plt.title("Wykres Lewy")
# plt.subplot(1,2,2)
# plt.barh(['A','B','C','D','E'],[-30,-32,-35,-33,-31],color=['pink','c','c','sienna','y'])
# plt.title("wykres prawy")
# plt.show()
# data=pd.read_excel('ceny2.xlsx')
# df=pd.DataFrame(data)
# print(data)
# print(df.groupby('Rodzaje towarów').agg({'Wartość':['mean']}))
# grupa=df[df['Rodzaje towarów']=='ryż - za 1kg'].groupby('Rok').agg({'Wartość':['sum']})
# print(grupa)
# grupa2=df[df['Rodzaje towarów']=='mąka pszenna - za 1kg'].groupby('Rok').agg({'Wartość':['sum']})
# # sns.relplot(data=grupa,x='Rok',y='Wartość',kind='line')
# # plt.annotate(text='166292',xy=(2010,3.3))
# data1=df[df['Rodzaje towarów']=='ryż - za 1kg']
# data2=df[df['Rodzaje towarów']=='mąka pszenna - za 1kg']
# # sns.relplot(data=data,x='Rok',y='Wartość',kind='line',hue='Rodzaje towarów')
# # plt.annotate(text='166292',xy=(2010,2.0))
# plt.plot(data1['Rok'],data1['Wartość'])
# plt.plot(data2['Rok'],data2['Wartość'])
# plt.show()
# data=pd.read_csv('nieruchomosci2.csv',sep=';',decimal=',',header=None)
#
# data=data.transpose()
# rynekp=data[data[0]=='rynek pierwotny']
# rynekw=data[data[0]=='rynek wtórny']
# plt.pie(rynekp[3],labels=rynekp[1])
#
# print(data)
# plt.show()
#zad1
# x=np.arange(0.1,3*np.pi,0.01)
# y1=np.log(x)
# plt.plot(x,y1,':',color='red',label='f(x)=log(x)')
# y2=3*x-5
# plt.plot(x,y2,'-.',color='green',label='f(x)=3x-5')
# y3=2*np.cos(x)
# plt.plot(x,y3,'--',color='pink',label='f(x)=2cos(x)')
# plt.grid()
# plt.title('Wykresy funkcji')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend()
# plt.savefig('wykres.png')
# plt.show()
#zad2
# data=pd.read_excel('mieszkania23.xlsx')
# df=pd.DataFrame(data)
# print(df)
# print(df.groupby('Formy budownictwa').agg({'Wartość':['sum']}))
# data1=df[df['Formy budownictwa']=='indywidualne']
# data2=df[df['Formy budownictwa']=='spółdzielcze']
# data3=df[df['Formy budownictwa']=='komunalne']
# plt.bar(data1['Rok']+0.00,data1['Wartość'],width=0.25,label='indywidulane')
# plt.bar(data2['Rok']+0.25,data2['Wartość'],width=0.25,label='komunalne')
# plt.bar(data3['Rok']+0.5,data3['Wartość'],width=0.25,label='spółdzielcze')
# plt.legend()
# plt.xticks(data['Rok'])
# plt.title('mieszkania')
# plt.xlabel('Rok')
# plt.ylabel('Wartość')
# plt.annotate(text='166292',xy=(2015,70000))
# plt.savefig('wykres2.pdf')
# plt.show()
#zad3
data=pd.read_excel('turystyka23.xlsx',header=None)
df=pd.DataFrame(data)
df=df.transpose()
print(df)
rok2014=df[df[1]=='2014']
plt.pie(rok2014[2],labels=rok2014[0],autopct='%.2f%%')
plt.savefig('wykres3.jpg')
plt.show()
