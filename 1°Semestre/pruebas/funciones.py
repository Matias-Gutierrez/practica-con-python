#Funcion para determinar el factorial de un numero
def factor(num: int):
    fact = 1
    for i in range(1, (num+1)):
        fact = fact * i
    return fact
def coefbino(num1: int, num2: int):
    numerador = factor(num1)
    deno_1 = factor(num2)
    deno_2 = factor((num1-num2))
    coef = (numerador/(deno_1*deno_2))
    return coef

# num1 = int(input("Ingrese un numero natural: "))
# print(f"El factor de {num1}! = {factor(num1)}") 
print("Introusca el numerador del coeficiente binomial")
n = int(input())
print("Ingrese el denominador del coeficiente binomial")
k = int(input())
print(f"El coeficiente binomial de {n} sobre {k} = {coefbino(n, k)}")