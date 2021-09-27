print("Saluados usuario, ingrese el numero del menu al que desea ingresar")
print("1= suma o resta, 2= potencia, 3 = promedio, presione cualquier otro numero para salir del programa")
menu=input()
if menu == "1":
    print("Que operacion desea realizar: suma ó resta")
    operacion = input()
    operacion = operacion.lower()
    if operacion == "suma":
        print("ingrese los valores a sumar")
        num1= int(input("Ingrese el primer valor: "))
        num2= int(input("Ingrese el segundo valor: "))
        suma=num1+num2       
        print("El resutado de",num1,"+",num2,"=",suma)
    elif operacion == "resta":
        print("ingrese los valores a restar")
        num1= int(input("Ingrese el primer valor: "))
        num2= int(input("Ingrese el segundo valor: "))
        resta=num1-num2       
        print("El resutado de",num1,"-",num2,"=",resta)
elif menu=="2":
    print("Ingrese los valores de la base y del exponente")
    num1= int(input("Ingrese el valor de la base: "))
    num2= int(input("Ingrese el valor del exponente: "))
    pot=num1**num2
    print("El resultado del exponente de base",num1,"con exponente",num2,"es igual a",pot)
elif menu=="3":
    print("Ingrese las notas a promediar")
    num1= int(input("Ingrese la nota al 80%: "))
    num2= int(input("Ingrese la nota al 20%: "))
    prom = num1*0.8 + num2*0.2
    print("El promedio entre",num1,"y",num2,"da como resultado:",prom)
print("Adios que tenga un buen dia")