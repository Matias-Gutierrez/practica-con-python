"""6.- Año bisiesto: Realizar un algoritmo que dado un año, este indique si es un año bisiesto
o no. Las condiciones son las siguientes:
a) Si es divisible por 4 y no es divisible por 100 es bisiesto.
b) Si un año es divisible entre 100 y además es divisible entre 400, también
resulta bisiesto."""

print("Ingrese un año")
año = int(input())
if (año%4)== 0 and (año%100) != 0:
    print("El año ingresado es un año bisiesto")
elif (año%100) == 0 and (año%400) == 0:
    print("El año ingresado es bisiesto")
else:
    print("El año no es bisiesto")