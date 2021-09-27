# !/usr/bin/python 
# -*- coding: utf-8 -*-
# Nombre del Autor:  

# Bibliotecas importadas

# Definir funciones
def separador(palabra):
    pares = []
    impares = []
    palabra = palabra.split(" ")
    for a in range(len(palabra)):
        if (a%2== 0):
            impares.append(palabra[a])
        else:
            pares.append(palabra[a])

    return pares, impares
# Codigo Principal

if __name__== "__main__" :
    print("Escriba una frase:")
    frase = input()
    resultado = separador(frase)
    print("Las palabras en posicion impar son :",' '.join([str(elem) for elem in resultado[1]]))
    print("Las palabras en posicion par son :",' '.join([str(elem) for elem in resultado[0]]))
    print(resultado[1])

