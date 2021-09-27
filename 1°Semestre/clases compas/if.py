""" Ingresar una temperatura en celcius y que el programa diga si hace frio ( cuando la temperatura es menor a 20°)
y cuando hace calor(cuando la temperatura el mayor o igual a 20°)
"""

print("Ingrese la temperatura actual")
celsius = int(input())

if celsius < 20:
    print("Hace frio culiao anda a abrigarte")
else:
    print("Hace calor weon anda ducharte a la pileta")
