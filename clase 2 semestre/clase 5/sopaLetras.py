# !/usr/bin/python
# -*- coding: utf-8 -*-
# Nombre del Autor: Matías Gutierrez

# Bibliotecas importadas

# Definir funciones



def lectura(nombreArchivo):
    prueba = open(nombreArchivo)
    totalLineas = sum(1 for line in prueba)
    prueba.close()
    lector = open(nombreArchivo)
    lineas = []
    for __nLinea__ in range(totalLineas):
        linea = (lector.readline()).rstrip()
        lineas.append(linea)
    lector.close()
    return lineas

def separador(lista):
    dimensiones = lista[0]
    y,x = dimensiones.split(" ")
    y = int(y)
    x = int(x)
    lista.pop(0)
    return x,y,lista

def listaMatris(sopabeta):
    sopalpha = []
    for linea in range(len(sopabeta)):
        comodin = sopabeta[linea]
        sopalpha.append(comodin.split(" "))
    return sopalpha
def buscador(archivol,sopa):
    lista = lectura(archivol)
    x,y,palabras = separador(lista)
    sopa = listaMatris(lectura(sopa))
    busqueda = []
    for palabra in palabras:

        largopalabra = len(palabra)
        for i in range(y):
            for j in range(x):
               # print(sopa[i][j])
                index = 0
                if palabra[0] == sopa[i][j]:
                    print(palabra)
                    index += 1
                    x1 = j
                    y1 = i
                    coincidencia = null
                    # palabra a la izquieda
                    # Evalua si es posible que la palabra este a la izquirda por la posicion y el largo de la palabra
                    if (largopalabra-1 <= (j+1)):
                        # Evalua si es que la segunda letra coincide con la letra a la izquierda
                        if palabra[index] == sopa[x1-1][y1]:
                            condicion = x1 + 2
                            index +=1
                            # Conprueba las demás letras
                            while (condicion != largopalabra-2):
                                if palabra[index]  != sopa[x1][y1]:
                                    condicion = largopalabra-3
                                    coincidencia = False
                                index +=1
                                x1 -= 1
                                condicion += 1
                    # palabra a la derecha
                    # Evalua si es posible que la palabra este a la derecha por la posicion y el largo de la palabra
                    if (largopalabra-1 <= (x-(x1+1))):
                        if palabra[index] == sopa[x1+1][y1]:
                            condicion = x1 + 2
                            index += 1
                            # comprueba las demás letras
                            while(condicion != largopalabra-2):
                                if palabra[index] != sopa[x1][y1]:
                                    condicion = largopalabra-3
                                    coincidencia = False

                                x1 += 1
                                index += 1
                                condicion += 1
                    # palabra hacia arriba
                    if(largopalabra+1<= (y1+1)):
                        if palabra[index] == sopa[x1][y1-1]:
                            condicion = y1 + 2
                            index += 1
                            # Comprueba las demás letras
                            while(condicion != largopalabra-2):
                                if palabra[index] != sopa[x1][y1]:
                                    condicion = largopalabra-3
                                    coincidencia = False

                                y1 -= 1
                                index += 1
                                condicion += 1
                    if (largopalabra-1 <= (y-(y1+1))):
                        if palabra[index] == sopa[x1][y1+1]:
                            condicion = y1 + 2
                            index += 1
                            # comprueba las demás letras
                            while(condicion != largopalabra-2):
                                if palabra[index] != sopa[x1][y1]:
                                    condicion = largopalabra-3
                                    coincidencia = False

                                y1 += 1
                                index += 1
                                condicion += 1

                    if coincidencia:
                        # print(palabra)
                        busqueda.append("encontrada")

            if coincidencia:

        if (not(coincidencia)):
            # print(palabra)
            busqueda.append("No encontrada")
    return busqueda
# Codigo Principal
if (__name__ == "__main__"):
    busqueda = buscador("sopa.txt","sopaletra.txt")
    print(busqueda)


















    asynic
