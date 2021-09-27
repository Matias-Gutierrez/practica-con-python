"""2.- Algoritmo que lea dos números e indique cual es mayor o si son iguales. """
print("Ingrese el primer valor")
numero1 = input()
print("Ingrese el segundo valor")
numero2 = input()
if numero1>numero2:
    print("El numero", numero1, "es mayor que",numero2)
elif numero2>numero1:
    print("El numero", numero2,"es mayor que",numero1)
if numero1 == numero2 :
    print("El numero",numero1,"es igual a", numero2)