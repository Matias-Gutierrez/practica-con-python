# !/usr/bin/python 
# -*- coding: utf-8 -*-
# Nombre del Autor: Matías Gutierrez

#  Bibliotecas importadas
import valnum 
# Definir funciones 

def validador(rut):
    # Iniciacion de variables de intancia 
    totalEvaluar = 0
    multiplicador = 2
    largo = len(rut)
    
    # Verficicacion de largo de rut sea valido
    if largo < 3:
        return False

    # Separa el rut en digito verificador y el rut 
    rut = rut.split("-")

    # Guarda el rut en la varable numRut y el digito verificador en digVerificador 
    numRut = rut[0] 
    digVerificador = rut[1]
    # Elimina los puntos en el numero del rut 
    numRut = numRut.replace(".","")

    # Evalua si en el numero del rut son solo numeros 
    if valnum.valnum(numRut)[0] == True:
        largorut = len(numRut)
        contador = 0
        evaluador = largorut-1
        while(contador < largorut):
            if multiplicador == 8:
               multiplicador=2
            totalEvaluar += (int(numRut[evaluador])) * multiplicador
            evaluador -=1
            multiplicador += 1
            contador += 1
        totalEvaluar = totalEvaluar % 11
        resultado = 11 - totalEvaluar
        if resultado == digVerificador:
            return True
        else:
            return False
    else:
        return False



# Código principal

if __name__ == "__main__":
    print("ingrese un rut")
    rut = input()
    valor = validador(rut)
    if (valor == True):
        print("El rut ingresado es valido")
    else: 
        print("El rut ingresado es invalido ")

    print("---Fin del Programas---")