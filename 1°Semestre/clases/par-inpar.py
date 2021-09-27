"""5.- Par o impar: Realizar un algoritmo que dado un número entero, indique en pantalla si
este es par o impar, si el número es igual a cero, se deberá indicar que es cero.
"""
print("Ingrese un numero entero")
num = int(input())

if (num%2)==0 and num!=0:
    print("El numero:", num ,"es un numero par")
elif num==0:
    print("El numero ingresado es cero")
else:
    print("El numero:",num, "es un numero inpar")