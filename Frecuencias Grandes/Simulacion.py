#!/usr/bin/env python

########################################### PAQUETES ###########################################

from math import pi, sin, cos
from decimal import Decimal
from tqdm import tqdm
import time
import os
import subprocess

########################################### FUNCIONES ###########################################

def ic(f,n): #da intervalos circulo
    return((f*2*pi)/n)

def valorx(da, m):
    return(round(cos(da*m+pi*0.5),4))

def valory(da, m):
    return(round(sin(da*m),4))

############################################# CODIGO #############################################

f1 = float(input("Indique la frecuencia de uno de los ejes: "))
f2 = float(input("Indique la frecuandia de el otro eje: "))
ntot=int(input("Indique la cantidad de puntos a dibujar: "))
lineas = input("¿Desea conectar los puntos con lineas? [s] ")
 
dax=ic(f1,ntot)
day=ic(f2,ntot)

file=open("plot.dat","w")


for i in range(0,ntot+1):
    x=valorx(dax,i)
    y=valory(day,i)
    file.write(str(x)+'      '+str(y)+'\n')
        
file.close()

if lineas == "s":
    os.system("gnuplot Lineas.gnuplot")
else:
    os.system("gnuplot Puntos.gnuplot")

os.system("eog output.gif")

save = input("¿Desea salvar el gif? [s/n] ")
if save == "s":
    if lineas == "s":
        name = 'L-'+str(f1)+'-'+str(f2)+'-'+str(ntot)+".gif"
        os.system("mv output.gif "+name)
        os.system("mv "+name+" ../GIFs/")
    else:
        name = 'P-'+str(f1)+'-'+str(f2)+'-'+str(ntot)+".gif"
        os.system("mv output.gif "+name)
        os.system("mv "+name+" ../GIFs/")