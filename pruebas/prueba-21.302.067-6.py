# !/usr/bin/python
# -*- coding: utf-8 -*-
# Nombre del Autor: Matías Gutierrez

# Bibliotecas importadas
import matplotlib.pyplot as plt

# Definir funciones
def lectura(nombreArchivo):
    archivo = open(nombreArchivo,"r")
    datosbruto = archivo.readlines()
    comunas = []
    casos = []
    for linea in datosbruto:
        datosSeparados = linea.split(",")
        if datosSeparados[1] == "07":
            nombreComuna = datosSeparados[2]
            comunas.append(nombreComuna)
            casostotales = datosSeparados[5].rstrip("\n")
            casostotales = float(casostotales)
            casos.append(casostotales)
    return comunas, casos
def graficar(x,y):
    fig,aux = plt.subplots()
    aux.bar(x,y)
    plt.show()

def datosDetalle(x,y):
    for index in range(len(x)):
        print(x[index]," contiene un total de", y[index],"casos registrados")
# Codigo Principal
if(__name__== "__main__"):
    x,y = lectura("casos_por_region.csv")
    graficar(x,y)
    datosDetalle(x,y)
