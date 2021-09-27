print("Ingrese un dato del tipo numerico:  ")
numero = input()
while (numero.replace(",", "")).isdigit() == False :
    print("El dato ingresado no es valido vuelva a intarlo")
    numero = input()
print("El numero ingresado es valido")

