# Crear un programa que ingrese dos valores de los va sumar y que el usuario pueda ingresar dos valores las veces que el quiera 
# Iniciamos nuestro condiciones para que en el ciclo while se inicie 
repeticion = 0 
respuesta = "si" 

while repeticion < 5 and respuesta == "si":
    # Pedimos los valores al usuario 
    print("Ingrese los siguientes valores a sumar")
    numero1 = int(input("Ingrese el primer valor: "))
    numero2 = int(input("Ingrese el segundo valor: "))
    
    # Creamos la variable que contiene la suma de los dos valores 
    suma = numero1 + numero2

    # Imprimimos en pantalla el resultado de la suma
    print("La suma de ",numero1,"+",numero2,"=",suma)

    # Le preguntamos al usuario si quiere ingresar otros valores a sumar
    print("Quiere hacer otra suma?")
    respuesta = input()
    respuesta = respuesta.lower()

    # Hacemos que una de las condiciones incremente para que se pueda salir del while después de 5 repeticiones
    repeticion = repeticion + 1