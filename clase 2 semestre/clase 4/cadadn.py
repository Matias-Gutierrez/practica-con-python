# !/usr/bin/python 
# -*- coding: utf-8 -*-
# Nombre del Autor: Matías Gutierrez

# Bibliotecas importadas

# Definir funciones
def buscador():
    archivo = open("cadenas.txt")
    linea = archivo.readline()
    linea = linea.split(" ")
    cadena1 = linea[0]
    cadena2 = linea[1]
    condicion1 = 0
    index1 = 0
    index2 = 0
    coincidente = ""
    largocoincide=0
    largo = 0
    repeticion = "" 
    for elem in range(len(cadena1)):
        condicion1 = 0
        while condicion1 < len(cadena2)-1:
            
            if cadena1[elem] == cadena2[condicion1]:
                index1 = elem
                index2 = condicion1
                while condicion1 < len(cadena2) and index1<(len(cadena1)) and index2 < len(cadena2):
                    
                    if cadena1[index1] == cadena2[index2]:
                        coincidente += cadena1[index1]
                    else:
                        
                        condicion1 += len(cadena2)
                        largocoincide = len(coincidente)
                    index1 +=1
                    index2 +=1
                    condicion1 +=1
                
                if largo < largocoincide:
                    repeticion = coincidente
                    largo = largocoincide
                
                coincidente = ""
            condicion1 += 1
        
    return repeticion
# Codigo Principal
if __name__=="__main__":
    resultado = buscador()
    print(resultado)