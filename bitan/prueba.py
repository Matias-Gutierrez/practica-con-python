# !/usr/bin/python
# -*- coding: utf-8 -*-
# Nombre del Autor: Matías Gutierrez

# Bibliotecas importadas
import matplotlib.pyplot as plt

# Definir funciones
def lectura(nombreArchivo):
    archivo = open(nombreArchivo,"r")
    datos = archivo.readlines()
    comunasmaule = []
    casoscovid = []
    for linea in datos:
        separaciondedatos = linea.split(",")
        if separaciondedatos[1] == "07":
            nombreComuna = separaciondedatos[2]
            comunasmaule.append(nombreComuna)
            casoscovidtotales = separaciondedatos[5].rstrip("\n")
            casoscovidtotales = float(casoscovidtotales)
            casoscovid.append(casoscovidtotales)
    return comunasmaule, casoscovid
def graficar(x,y):
    fig,aux = plt.subplots()
    aux.bar(x,y)
    plt.show()

def datosDetalle(x,y):
    for index in range(len(x)):
        print(x[index]," contiene un total de", y[index],"casoscovid registrados")
# Codigo Principal
if(__name__== "__main__"):
    x,y = lectura("casos_por_region.csv")
    graficar(x,y)
    datosDetalle(x,y)
