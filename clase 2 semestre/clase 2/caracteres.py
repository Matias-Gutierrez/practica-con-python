# !/usr/bin/python 
# -*- coding: utf-8 -*-
# Nombre del Autor: Matías Gutierrez

# Bibliotecas importadas

# Definir funciones
def contador(frase):
    vocala= frase.count("a")
    vocale= frase.count("e")
    vocali= frase.count("i")
    vocalo= frase.count("o")
    vocalu= frase.count("u")
    caracteres = 0
    
    vocalesTotales= vocala+vocale+vocali+vocalo+vocalu
    frase = frase.split(" ")

    for a in frase:
        print(a)
        caracteres += len(a)
        print(caracteres)
    return caracteres,vocalu,vocala,vocale,vocali,vocalo,vocalesTotales
# Codigo Principal
if __name__ == "__main__":
    print("Ingrese una frace")
    frase = input()

    resultado = contador(frase)

    porceA = resultado[2]/resultado[6]
    porceE = resultado[3]/resultado[6]
    porceI = resultado[4]/resultado[6]
    porceO = resultado[5]/resultado[6]
    porceU = resultado[1]/resultado[6]

    
    porceVocales = resultado[6]/resultado[0]

    print(f"El procentaje de vocales que hay en el texto son {porceVocales}%")
    print(f"El porcentaje de vocales a es de {porceA}%")

    