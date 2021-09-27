""" 
Ingresar una temperatura en celcius y que el programa diga si hace frio ( cuando la temperatura es menor a 20°)
y cuando hace calor(cuando la temperatura el mayor o igual a 20°)
"""
print("Ingrese la temperatura")
temp = int(input())
if temp < 20:
    print("Hace frio")
elif temp == 20:
    print("Esta templado")
else:
    print("Hace calor")

# Distinto -->   !=
# Igual --> ==
# Mayor >
# Mayor o igual >=
# Menor <
# Menor o igual <=