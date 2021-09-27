"""Escriba un programa que solicite una contraseña 
(el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan. """
# Creamos una condicion para evaluar en el while y que se pueda ejecutar
condicion = 0


while condicion == 0:

    print("Cree una contraseña")
    
    contraseña1 = input("Ingrese su contraseña: ")
    contraseña2 = input("Ingrese denueva su contraseña: ")

    if contraseña1 == contraseña2 :
        print("Contraseña aceptada")
        condicion = 1
    else:
        print("contraseñas no coiciden, vuelva a ingresarlas")