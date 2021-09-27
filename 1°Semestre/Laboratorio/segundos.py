ingre = int(input("Ingrese los segundos a transformar: "))
segundos = ingre%60
minutos = ingre//60
hora = minutos//60
minutos = minutos%60
print("La transformacion de ", ingre," a hora:minutos:segundos es ", hora,":", minutos,":",segundos)