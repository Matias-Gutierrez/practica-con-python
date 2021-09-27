""" Crear un programa que pida el nombre y el primer apellido
y que retorne un saludos de bienvenida con su nombre y apellidos con las primera letra de estos en mayuscula """
# Definimos la función llamada cambio y le definimos la variable de entrada
def cambio(nombre):
    # Aqui definimos lo que realizara la funcion con su valor de entrada
    nombre=nombre.lower()
    nombre=nombre.title()
    # Con el return definimos el valor de retorno de la función
    return nombre

print(" ingrese su primer nombre")
Nombre = cambio(input())
print("ingrese su primer Apellido")
apellido= cambio(input())
print("Hola ", Nombre, apellido, "bienvenido a la aplicación")