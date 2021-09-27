"""El usuario ingrese un valor y que el programa lo replace en la siguiente ecuacion X^3 + 3x + 25
"""
var=int(input("Ingrese un numero a evaluar en la ecuación: "))
final = var**3 + var*3 + 25
print("El valor de la ecuacion cuando se evalua en",var,"tiene un valor final de ",final)