# !/usr/bin/python 
# -*- coding: utf-8 -*-
# Nombre del Autor: Matías Gutierrez

# Bibliotecas importadas

# Definir funciones
numeros = ["7777","9999","222","333","444","555","666","777","888","999","22","33","44","55","66","77","88","99","2","3","4","5","6","7","8","9","0"]
letras = ["s","z","c","f","i","l","o","r","v","y","b","e","h","k","n","q","u","x","a","d","g","j","m","p","t","w"," "]
def cambio_mensaje(mensaje):
    mensaje = mensaje.lower()
    cambio = ""
    for i in mensaje:
        cambio += numeros[letras.index(i)]
    return cambio
def cambio_num(mensaje):
    
# Codigo Principal
if (__name__=="__main__"):
    numeros = input("Ingrese el mensaje: ")
    print(cambio_mensaje(numeros))