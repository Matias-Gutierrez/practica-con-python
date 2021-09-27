"""
Crear un programa que pida que se ingrese una cantidad de notas a ingresar, seguido pida las notas y luego que saque el promedio.
"""
notas = []

def ingresoNotas(cantidadnotas):
    contador = 0
    while (contador<cantidadnotas):
        entrada = float(input())
        notas.append(entrada)
        contador+=1


def promedio(cantnotas):
    sumatoria = 0
    for nota in notas:
        sumatoria+= nota
    prome = sumatoria/cantnotas
    return prome

if(__name__ == "__main__"):
    print("ingrese la cantidad de notas a ingresar")
    cantnotas = int(input())
    ingresoNotas(cantnotas)
    prome = promedio(cantnotas)
    print(prome)