# !/usr/bin/python
# -*- coding: utf-8 -*-
# Nombre del Autor: Matías Gutierrez

# Bibliotecas importadas

# Definir funciones
def Lectura(nArchivo):
    archivo = open(nArchivo,"r")
    lineas = archivo.readlines()
    archivo.close()
    for linea in lineas:
        separacion = (linea.rstrip("\n")).split(",")
        if(separacion[0] == "Maule"):
            rMaule = separacion
    return rMaule

def porcentaje(maule,personasRegionMaule):
    personasInfectadasAcumuladas = int(maule[1])
    personasReinfectadas = personasInfectadasAcumuladas * 0.08
    personasAcumuladas = personasInfectadasAcumuladas - personasReinfectadas
    porcentajeInfectadas = ((personasAcumuladas) * 100)/personasRegionMaule
    return porcentajeInfectadas

def PorMuertos(Maule,personasMaule):
    muertos = int(Maule[2])
    porcetajeMuertos = (muertos*100)/personasMaule
    return porcetajeMuertos

def ProbMuerte(nombreArchivo):
    archivo = open(nombreArchivo)
    lineas = archivo.readline()
    lineas = archivo.readlines()
    archivo.close()
    regiones = []
    proba = []
    repeticion = 0
    while(repeticion != 15):
        linea = lineas[repeticion]
        datos = (linea.rstrip("\n")).split(",")
        region = datos[0]
        probabilidad = (int(datos[2])*100)/int(datos[1])
        regiones.append(region)
        proba.append(probabilidad)
        repeticion += 1
    reg = 0
    prob = 0
    for indice in range(len(region)):
        if proba[indice] > prob:
            reg = regiones[indice]
            prob = proba[indice]
    return reg, prob

# def PorcentajeMuerte():
# Codigo Principal

if __name__ == "__main__":
    rMaule = Lectura("CasosConfirmados-totalRegional.csv")
    personasRegionMaule = 908097
    porInfectadas = porcentaje(rMaule,personasRegionMaule)
    porInfectados = format(porInfectadas,".2f")
    print(f"El porcentaje de infectados en la region del Maule es del {porInfectados}%")
    porMuertos = PorMuertos(rMaule,personasRegionMaule)
    porMuertos = format(porMuertos,".2f")
    print(f"El porcentaje de muerte por covid en la region del Maule es del {porMuertos}%")
    region, probabilidad = ProbMuerte("CasosConfirmados-totalRegional.csv")
    probabilidad = format(probabilidad,".2f")
    print(f"El porcentaje mas alto de muerte por covid es en la Region de {region}, con una probabilidad de {probabilidad}")
