#Definimos la función bisies la cual evalua si un año es biciesto 
def bisies(año):
    if (año%4)== 0 and (año%100) != 0:
        return 1
    elif (año%100) == 0 and (año%400) == 0:
        return 1
    else:
        return 0 
# Aqui hacemos el ingreso de variables
print("Ingrese su fecha de nacimiento")
añonacimiento = int(input("Ingrese su año de nacimiento: "))
dianac = int(input("ingrese su dia de nacimiento: "))
mesnacimiento = int(input("ingrese su mes de nacimiento: "))
print("Ahora ingrese la fecha actual")
añoactual = int(input("Ingrese el año actual: "))
diaact = int(input("ingrese el dia actual: "))
mesactual = int(input("ingrese el mes actual: "))


años = (añoactual-añonacimiento)
añoevaluar = añonacimiento
# Creamos la función for para calcular los años bisiestos vividos
for i in range(años):
    añosrecorridos = añoevaluar + i
    diabisiesto = diabisiesto + bisies(añosrecorridos)

if mesnacimiento == mesactual:
    if dianac == diaact: 
        dias = (añonacimiento-añoactual)*365
        