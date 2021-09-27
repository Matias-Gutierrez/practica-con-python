print("Bienvenido por el cambio de politicas del hospital, ingrese los sguientes datos:")
categoria = int(input("Ingrese la categoria a la que pertence el paciente:  "))
edad = int(input("Ingrese la edad del paciente:  "))
cdias = int(input("ingrese la cantidad de dias que lleva el paciente: "))
if categoria == 1:
     totalapagar=120
if categoria == 2:
     totalapagar=150
if categoria == 3:
     totalapagar=170
if categoria == 4:
     totalapagar=200

totalapagar = totalapagar*cdias

if edad <10 or edad>70:
    aumento= totalapagar*0.2
    totalapagar= totalapagar+aumento
print("El paciente debera pagar $",totalapagar)