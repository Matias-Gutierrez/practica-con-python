print("Saludos profesor, cuantos alumnos desea ingresar a la nomina")
alumnos= int(input())
contador = 1
nombres = []
rut = []
nota = []
while contador <= alumnos:
    print("Ingrese el nombre del alumno")
    nombres.append(input().title())
    contador +=1
    print("Ingrese el rut del alumno")
    rut.append(input().title())
    print("Ingrese el la nota del alumno")
    nota.append(int(input()))

for i in range(alumnos):
    print(f"El alumno {nombres[i]} tiene en su registro de notas la siguiente nota {nota[i]}")

