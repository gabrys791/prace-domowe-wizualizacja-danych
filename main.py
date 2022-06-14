import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#zad1
# plt.subplots(1,2)
# x=['A','B','C','D','E']
# y=[-35,-20,-50,-35,-45]
# y1=[37,37,40,31,35]
# plt.subplot(1,2,1)
# plt.barh(x,y,color=['lime','gold','blue','mediumpurple','indianred'])
# plt.xticks(np.arange(-50,0,10))
# plt.title('Wykres1')
# plt.subplot(1,2,2)
# plt.barh(x,y1,color=['darkkhaki','mediumpurple','darkorange','green','darkkhaki'])
# plt.title('Wykres2')
# plt.savefig('wykres1.pdf')
# plt.show()
#zad2
# data=pd.read_csv('ceny3.csv',sep='#',decimal=',')
# df=pd.DataFrame(data)
# print(df.groupby('Rodzaje towarów i usług').agg({'Wartosc':['mean']}))
# print(df)
# maka=df[df['Rodzaje towarów i usług']=='mąka pszenna - za 1kg']
# ryz=df[df['Rodzaje towarów i usług']=='ryż - za 1kg']
# plt.bar(ryz['Miesiące'],ryz['Wartosc'],label='Ryż')
# plt.bar(maka['Miesiące'],maka['Wartosc'],label='Mąka')
# plt.xticks(rotation=45)
# plt.legend()
# plt.ylabel('wartość')
# plt.xlabel('miesiące')
# plt.title('Wartości ryżu i mąki')
# plt.annotate(text='166292',xy=('grudzień',0.1))
# plt.savefig('wykres2.jpg')
# plt.show()
#zad3
data=pd.read_excel('handel3.xlsx',header=None)
data=data.transpose()
print(data)
rok16=data[data[1]=='2016']
rok17=data[data[1]=='2017']
print(rok16)
plt.subplots(1,2)
plt.subplot(1,2,1)
plt.pie(rok16[2],labels=rok16[0],startangle=60,rotatelabels=True,autopct='%1.1f%%')
plt.title('2016')
plt.subplot(1,2,2)
plt.pie(rok17[2],labels=rok17[0],startangle=45,rotatelabels=True,autopct='%1.1f%%')
plt.title('2017')
plt.savefig('wykres3.png')
plt.show()