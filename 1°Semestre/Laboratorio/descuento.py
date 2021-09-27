sueldo = int(input("Ingrese el sueldo del trabajador para calcular su sueldo final: "))
if sueldo > 3000000:
    sueldo = sueldo - (sueldo*0.15)
if sueldo <=3000000 and sueldo >= 1000000 :
    sueldo = sueldo - (sueldo*0.1)
if sueldo > 500000 and sueldo < 1000000:
    sueldo = sueldo - (sueldo*0.05)
print("El sueldo que recibira el trabajador mas el descuento sera de: ",sueldo )