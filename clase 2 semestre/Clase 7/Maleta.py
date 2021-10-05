# !/usr/bin/python
# -*- coding: utf-8 -*-
# Nombre del Autor: Matías Gutierrez

# Bibliotecas importadas

# Definir funciones
def Lectura(entrada):
    entrada = open(entrada)
    entradas = []
    for linea in entrada:
        linea = linea.lower()
        larPalabra = len(linea)
        if larPalabra <= 20:
            if linea.count("i") ==0:
                entradas.append("S")
            else:
                entradas.append("N")
        else:
            palabraPermitida = linea[:19]
            if palabraPermitida.count("i") == 0:
                entradas.append("S")
            else:
                entradas.append("N")
    entrada.close()
    salida = open("Salida.txt","w")
    for respuesta in entradas:
        salida.write(respuesta+"\n")
    salida.close()

    return entradas
# Codigo Principal
if __name__=="__main__":
    Lectura("entrada.txt")
