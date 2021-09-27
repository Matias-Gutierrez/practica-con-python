# !/usr/bin/python 
# -*- coding: utf-8 -*-
# Nombre del Autor: Matías Gutierrez

# Bibliotecas importadas

# Definir funciones
def lenguajeMorse(texto):
    morse ={
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", 
    "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", 
    "m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".--.", "q": "--.-",
    "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
    "x": "-..-", "y": "-.--", "z": "--..", " ":"/"
    }
    textoTraducido = ""
    for c in texto:
        if c != " " and c.lower() in morse:
            textoTraducido += morse[c.lower()]
        else:
            textoTraducido += c
    return textoTraducido

def MorseLenguaje(texto):
    morseinver = {
        ".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e", "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j", "-.-":"l", "--":"m",
        "-.":"n", "--.--":"ñ", "---":"o", ".--.":"p" , "--.-":"q",".-.":"r", "...":"s", "-":"t", "..-":"u", "...-":"v", ".--":"w", "-..-":"x",
        "-.--":"y", "z":"--.."," ":"/"
    }

    if texto.count("/") == 0:
        return False
    textoTraducido = ""
    texto = texto.split("/")
    for c in texto:
        if c != " " and c.lower() in morseinver:
            textoTraducido += morseinver[c.lower()]+"/"
        else:
            textoTraducido += c
    return textoTraducido

    
# Codigo Principal
if (__name__=="__main__"):
    condicion = 0
    while (condicion != 1):
        print("Escriba que quiere hacer")
        print("m = de morse a latin, l = de latin a morse")
        opcion = input()
        if (opcion == "m"):
            print("Ingrese cada codigo separado por / y los espacios con // ")
            texto = input()
            resultado = MorseLenguaje(texto)
            if resultado == False:
                print("El codigo no contiene el formato solicitado")
            else:
                print("El codigo:")
                print(texto)
                print("Se traduce en esto,\n",resultado)
                condicion = 1
        elif(opcion=="l"):
            print("ingrese el texto a traducir")
            entrada = input()
            resultado = lenguajeMorse(entrada)
            print(resultado)
            condicion = 1
        else:
            print("Opcion ingresado no es valida")