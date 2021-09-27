"""
El usuario intrusca la cantidad de numeros que ingresara y
que los numeros ingresados se sumen y luego muestre los numeros y el resultado de la suma entre ellos
"""
numeros=[]
def entrada_numeros(num):
    contador = 0
    while(contador< num):
        print("ingrese el numero")
        entrada = int(input())
        numeros.append(entrada)
        contador += 1

def sumanumeros():
    sumatoria = 0
    for numero in numeros:
        sumatoria += numero
    return sumatoria, numeros

if(__name__=="__main__"):
    print("ingrese la cantidad de numeros a ingresar")
    cantidad = int(input())
    entrada_numeros(cantidad)
    for elem in numeros:
        print(elem)
    print("La suma de todos los numeros ingresado es =", sumanumeros())