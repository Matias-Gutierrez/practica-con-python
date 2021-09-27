#Definimos la función bisies la cual evalua si un año es biciesto 
def bisies(año):
    if (año%4)== 0 and (año%100) != 0:
        return 1
    elif (año%100) == 0 and (año%400) == 0:
        return 1
    else:
        return 0 
# Ingreso de valores de parte del usuario 
print("Ingrese su fecha de nacimiento")
añonacimiento = int(input("Ingrese su año de nacimiento: "))
dianac = int(input("ingrese su dia de nacimiento: "))
mesnacimiento = int(input("ingrese su mes de nacimiento: "))
print("Ahora ingrese la fecha actual")
añoactual = int(input("Ingrese el año actual: "))
diaact = int(input("ingrese el dia actual: "))
mesactual = int(input("ingrese el mes actual: "))

# Creamos la variable que contendra los dias bisiestos que vivimos
diabisiesto = 0

# Creamos la variabe que contendra los dias vividos en el año de nacimiento
diasrecnac = 0

# Creamos la variable que contendra los dias de los meses restantes del año de nacimiento
diasmes_nac_vivido = 0

# Creamos la variable que contendra los dias de los años vivividos sin contar el año nacimiento y año actual
diaañovivi = 0

# Creamos la variable que contendra los dias de los meses vividos del año actual
diasañoact = 0

# Creamos la variable que contiene que la cantidad de años vividos
años = (añoactual-añonacimiento)
añoevaluar = añonacimiento
if mesnacimiento >2:
    añoevaluar = añonacimiento+1
    años -= 1

# Creamos la función for para calcular los años bisiestos vividos
for i in range(años):
    añosrecorridos = añoevaluar + i
    diabisiesto = diabisiesto + bisies(añosrecorridos)
# Calculamos si estamos despues de febrero y si el año actual es bisiesto
    if mesactual >2:
        if bisies(añoactual)==1:
            diabisiesto+=1
# Calculamos los dias del mes de nacimiento que vivio
if mesnacimiento == 1 or mesnacimiento == 3 or mesnacimiento == 5 or mesnacimiento == 7 or mesnacimiento == 8 or mesnacimiento == 9 or mesnacimiento == 12:
    dia_ref_nacimi = dianac
    diasrecnac = 31-dia_ref_nacimi
elif mesnacimiento ==4 or mesnacimiento == 6 or mesnacimiento == 9 or mesnacimiento == 11:
    dia_ref_nacimi = dianac
    diasrecnac = 30-dia_ref_nacimi
elif mesnacimiento ==2:
    dia_ref_nacimi = dianac
    diasrecnac = 28-dia_ref_nacimi
# Calculamos los dias vividos en el año de nacimiento
rang_mesevaluar = (12 - mesnacimiento)
diasmes_nac_vivido = 0

for i in range(rang_mesevaluar):
    mesaevaluar = (mesnacimiento+1)+i
    
    if mesaevaluar == 1 or mesaevaluar == 3 or mesaevaluar == 5 or mesaevaluar == 7 or mesaevaluar == 8 or mesaevaluar == 10 or mesaevaluar == 12:
        diasmes_nac_vivido = diasmes_nac_vivido+ 31
    elif mesaevaluar == 4 or mesaevaluar == 6 or mesaevaluar == 9 or mesaevaluar == 11:
        diasmes_nac_vivido = diasmes_nac_vivido+ 30
    elif mesaevaluar == 2: 
        diasmes_nac_vivido = diasmes_nac_vivido + 28
# Calculamos los dias de los años vividos
diaañovivi = (añoactual-1)-(añonacimiento+1)
diasviv =0
for i in range(diaañovivi):
    diasviv += 365
# Calcularemos los dia vividos en el año actual
mesacteva = mesactual
for i in range(mesacteva):
    mesaevaluar = i
    if mesaevaluar == 1 or mesaevaluar == 3 or mesaevaluar == 5 or mesaevaluar == 7 or mesaevaluar == 8 or mesaevaluar == 10 or mesaevaluar == 12:
        diasañoact += 31
    elif mesaevaluar == 4 or mesaevaluar == 6 or mesaevaluar == 9 or mesaevaluar == 11:
        diasañoact +=30
    elif mesaevaluar == 2:
        diasañoact +=28
diasvividos = diasrecnac + diasmes_nac_vivido + diasviv + diasañoact + diaact + diabisiesto
print(diasvividos)