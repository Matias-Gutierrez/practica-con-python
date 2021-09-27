"""Escriba un programa que solicite una contraseña y la vuelva a solicitar hasta que las dos contraseñas coincidan, con un límite de tres peticiones."""
condicion = 1
intentos = 1
while condicion !=0 and intentos <=3:
    print("Cree una contraseña")
    cont1=input("Ingrese nueva contraseña: ")
    cont2=input("Ingrese nuevamente la contraseña: ")
    if cont1 == cont2:
        print("contraseña creada ")
        condicion = 0
    intentos +=1