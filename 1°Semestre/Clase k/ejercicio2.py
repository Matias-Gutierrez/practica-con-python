"""Escriba un programa en el ingrese un numero y el programa determine si es par inpar o cero"""
pares = 0
inpares = 0
ceros = 0
while ceros == 0:
    print("Ingrese un numero")
    num = int(input())
    if num%2 == 0 and num != 0:
        pares += 1
    elif num%2 == 1:
        inpares += 1
    else:
        ceros = 1
print(f"Los numeros pares son {pares}")
print(f"Los numeros inpares son {inpares}")
print(f"Los numeros ceros son {ceros}")