import time
start_time = time.time()

#%%
from copy import deepcopy as cp
import matplotlib.pyplot as plt
from math import sqrt as sq
from math import factorial as fac
from math import inf
import random

#%%
class Punct():
    def __init__(self,nume,x,y,numar=0):
        self.nume=nume
        self.x=x
        self.y=y
        self.distante=[]
        self.numar=numar

def citire(fisier,lista):
    i=0
    for lines in fisier:
        words=lines.split()
        punct=Punct(words[0],int(words[1]),int(words[2]))
        lista.append(punct)
        punct.numar=i
        i+=1

def calc_dist(punctCurent,listaPuncte):
    for punctComparatie in listaPuncte:
        distanta=sq((punctComparatie.x-punctCurent.x)*(punctComparatie.x-punctCurent.x)+
        (punctComparatie.y-punctCurent.y)*(punctComparatie.y-punctCurent.y))
        tuplet=(punctComparatie.nume,round(distanta,2),punctComparatie.numar)
        punctCurent.distante.append(tuplet)

class Drum():
    def __init__(self):
        self.listaDrumuri=[]
        self.distantaTotala=0

def scr(orig):
    firstItem=orig.pop(0)
    dest = orig[:]
    random.shuffle(dest)
    dest.insert(0,firstItem)
    return dest
#%%
scoli=[]
tested=[]
#%%
F = open("data.txt","r")
citire(F,scoli)
plt.subplot(211)
#%%
for punct in scoli:
    calc_dist(punct,scoli)
    plt.plot(punct.x, punct.y,'-o',label="Locatiile scolilor")
exdrum=list(range(len(scoli)))
plt.axis([-100,100,-100,100])
# for punct in scoli:
#     print (punct.nume)
#     print (punct.distante)

#%%
solutie=Drum()

punctInitial=scoli.__getitem__(0)
punctCurent=punctInitial
solutie.distantaTotala=inf
ciclu=0
while (ciclu <=5000):
    if exdrum not in tested:
        tested.append(cp(exdrum))
        drum=Drum()
        drum.listaDrumuri.append(punctInitial)
        punctCurent=punctInitial
        for nr in exdrum:
            for nume,distanta,numar in punctCurent.distante:
                test=cp(scoli)
                if (nr == numar) and (distanta != 0):
                    punctCurent=test.pop(nr)
                    drum.listaDrumuri.append(punctCurent)
                    drum.distantaTotala+=distanta
        if(solutie.distantaTotala > drum.distantaTotala):
            solutie=cp(drum)
    exdrum=scr(exdrum)
    ciclu+=1

xsol=[]
ysol=[]
plt.subplot(212)
print("Drumul gasit este:",end='')
for dr in solutie.listaDrumuri:
    print (dr.nume,end = " ")
    plt.plot(dr.x, dr.y,'-o')
    xsol.append(dr.x)
    ysol.append(dr.y)
plt.plot(xsol,ysol,marker='+')
plt.suptitle('Drumul la scoli')
plt.axis([-100,100,-100,100])
plt.show()
print ()
print("Cu distanta totala de:",end='')
print (solutie.distantaTotala)

print("--- %s seconds ---" % (time.time() - start_time))