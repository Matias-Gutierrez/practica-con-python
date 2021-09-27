# !/usr/bin/python 
# -*- coding: utf-8 -*-
# Nombre del Autor: Matías Gutierrez

# Bibliotecas importadas

# Definir funciones
def valPangramas(palabra):
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","v","w","x","y","z"]

    palabra = palabra.lower()
    
    palabra = palabra.replace("á","a")
    palabra = palabra.replace("é","e")
    palabra = palabra.replace("í","i")
    palabra = palabra.replace("ó","o")
    palabra = palabra.replace("ú","u")
    palabra = palabra.replace("ü","u")
    palabra = palabra.replace("ñ","n")
    
    for ele in letras:
        if palabra.count(ele) == 0:
            return False
    return True

    
# Codigo Principal
if (__name__=="__main__"):
    entrada = input()
    resultado = valPangramas(entrada)
    if (resultado):
        print("Si es un pangrama")
    else:
        print("No es un pangrama")