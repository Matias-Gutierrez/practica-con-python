"""Crear un programa que te pregunte si quiere terminar con el programa.En caso que responda si se termina el programa"""
condicion="no"
while condicion != "si":
    print("Quiere que el programa termine")
    condicion = input()
    condicion = condicion.lower() 
print("-----------Fin del programa-----------") 