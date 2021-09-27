# !/usr/bin/python 
# -*- coding: utf-8 -*-
# Nombre del Autor: Esteban Barrios

import matplotlib.pyplot as plt

def lectura(nombre):
    archivo = open(nombre,"r")
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
    
def grafico(x,y):
    fig,aux = plt.subplots()
    aux.bar(x,y)
    plt.show()

def detalle_de_datos(x,y):
    for index in range(len(x)):
        print(x[index]," contiene un total de", y[index],"casos registrados")


#CodigoPrincipal
if(__name__== "main"):
    x,y = lectura("casos_por_region.csv")
    grafico(x,y)
    detalle_de_datos(x,y)