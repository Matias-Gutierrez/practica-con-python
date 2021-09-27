num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
resultado = 0
for i in range(num2):
    resultado += num1
print()
print(f"El resultado de {num1} x {num2} = {resultado} ")