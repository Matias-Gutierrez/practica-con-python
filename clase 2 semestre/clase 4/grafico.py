# !/usr/bin/python 
# -*- coding: utf-8 -*-
# Nombre del Autor: Matías Gutierrez

# Bibliotecas importadas
import matplotlib.pyplot as plt

# Definir funciones
def lectura():
    archivo = open("TotalesNacionalesResumen.csv")
    lineax = archivo.readline()
    lineay = archivo.readline()
    lineax = lineax.rstrip("\n")
    lineay = lineay.rstrip("\n")
    lineax = lineax.split(",")
    lineay = lineay.split(",")
    return lineax,lineay


def separador():
    lineax,lineay = lectura()
    if (len(lineax) == len(lineay)):
        for elem in range(len(lineay)):
            comodin  = lineay[elem]
            lineay.pop(elem)
            lineay.insert(elem,float(comodin))
        return lineax , lineay
    else:
        return False
def datos_casos(x,y):
    x1 = []
    y1 = []
    mes = x[0]
    # 2020-03-03
    # 0123456

    x1.append(mes[0:7])
    fecha_mes = 0 
    suma_casos = 0
    for fecha in range(len(x)):

        
        if x[fecha].startswith(x1[fecha_mes]):
            suma_casos += y[fecha]
        else:
            y1.append(suma_casos)
            suma_casos=y[fecha]
            fecha_mes+=1
            mes = x[fecha]
            x1.append(mes[0:7])

    y1.append(suma_casos)
    
    return x1, y1

def graficar(x,y):
    fig,aux = plt.subplots()
    aux.plot(x,y)
    plt.show()


# Codigo Principal
if(__name__=="__main__"):
    x,y = separador()
    
    # x1,y1 = datos_casos(x,y)
    graficar(x, y)