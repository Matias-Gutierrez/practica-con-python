"""El usuario ingrese un numero entero y el programa indique si el numero es positivo, negativo o cero
"""

print("Ingrese un numero entero")
num = int(input())

if num >0:
    print("El numero ingresado es positivo")
elif num <0:
    print("El numero ingresado es negativo")
else:
    print("El numero ingresado es igual a cero")