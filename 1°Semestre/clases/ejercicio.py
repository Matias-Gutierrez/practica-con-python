""" Crear un programa que pida el nombre y el apellido por separado
y que retorne un saludos de bienvenida con su nombre y apellido  con las primera letra de estos en mayuscula """
def cambio(nombre):
    return nombre.title()
print("Hola, ingrese su primer nombre")
nombre = input()
apellido = input()
Nombre = cambio(nombre)
Apellido = cambio(apellido)
print("Bienvenido", Nombre,Apellido, "a tinder" )

