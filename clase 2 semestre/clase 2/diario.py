# !/usr/bin/python 
# -*- coding: utf-8 -*-
# Nombre del Autor: Matías Gutierrez

# Bibliotecas importadas
# hola amigos de Youtube como estan. espero que se encuentren muy bien. saludos y comenten.
# Definir funciones
def reorganizar(entrada):
    entrada = entrada.capitalize()
    for carac in range(len(entrada)):
        if entrada[carac: carac+2] == ". ":
            print(entrada[carac +2])
            
    return entrada
# Codigo principal
if __name__ == "__main__":
    print("Escriba su entrada para el diario de vida")
    entrada = input("* ")
    resultado = reorganizar(entrada)
    print(resultado)
    