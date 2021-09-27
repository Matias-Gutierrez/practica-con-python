# El valor de una idea radica en el Uso de la misma
# El hombre ws el único Animal que come Sin tener hambre bebe Sin tener sed y habla Sin tener nada que decir
# Eres lo que haces No lo que dices que vas a Hacer 

# Pide al usuario ingresar una frase
print("Ingrese una frase: ")
palabra = input()

contare = palabra.count("e")
contara = palabra.count("a")

contarminus = 0
contarmayus = 0
lista = palabra.split(" ")

for mayusculas in lista:
    if mayusculas.istitle() == True:
        contarmayus += 1

for minusculas in lista:
    if minusculas[0].islower() == True:
        contarminus += 1

print(f"El numero de letras a en {palabra} es de {contara}")
print(f"El numero de letras e en {palabra} es de {contare}")

print(f"El numero de palabras con mayusculas y minusculas son {contarmayus} palabras")
print(f"El numero de palabras con solo minusculas es de {contarminus} palabras")

