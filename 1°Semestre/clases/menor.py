"""Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado."""
print("Ingrese un numero")
menor=int(input())
condicion=0
if menor ==0:
    condicion=1
while condicion == 0:
    print("Ingrese un numero")
    numero = int(input())
    if menor < numero:
        menor = numero
    if numero == 0:
        condicion = 1
print("El numero mas bajo ingresado es el numero", menor)
    