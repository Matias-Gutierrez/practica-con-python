"""
Crear un programa que te pregunte si quiere terminar con el programa.
En caso que responda si se termina el programa
"""
condicion = "si"
while condicion != "si":
    print("¿Quiere terminar con el programa?")
    condicion = input().lower()
    print(condicion)
print("---Fin del programa---")