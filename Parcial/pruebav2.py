# !/usr/bin/python
# -*- coding: utf-8 -*-
# Nombre del Autor: Matías Gutierrez

# Bibliotecas importadas
import pandas as pd
import matplotlib.pyplot as plt
# Definir funciones
def LecturaDatos(nomArchivo):
    datos = pd.read_csv(nomArchivo)
    filtros = ["Region","idRegion","Comuna","nose","numPersonas","casostotales"]
    datos.columns = filtros
    matris = datos[datos["Region"]=="Maule"]
    Comunas = matris["Comuna"].tolist()
    Casos = matris["casostotales"].tolist()
    return Comunas, Casos

def graficar(x,y):
    fig,aux = plt.subplots()
    aux.bar(x,y)
    plt.show()

def DetalleDatos(x,y):
    for index in range(len(x)):
        print(f"{x[index]} tiene {y[index]} casos totales")
# Codigo Principal
if(__name__=="__main__"):
    x,y = LecturaDatos("casos_por_region.csv")
    graficar(x,y)
    DetalleDatos(x,y)
