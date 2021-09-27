"""
Escribir una función que aplique un descuento a un precio y otra que aplique
el IVA a un precio. Una tercera funcion que ingrese los productos con su descuento, en caso de no
haber descuento debe ingresar cero.
"""

# funcion para aplicar descuento
def aplicarDescuento(precio, descuento):
    restar = (precio * (descuento/100))
    preciofinal = precio - restar
    return preciofinal
# funcion para aplicar el iva
def iva(precio):
    poriva = precio * 0.19
    precioFinal = precio + poriva
    return precioFinal
# funcion lista de productos
def lista(cantProductos):
    itera = 0
    preciofinal= 0
    listacompra = []
    while( cantProductos > itera):
        print("Ingresa el precio")
        precio = int(input())
        print("ingrese el descuento en porcentaje")
        descuento = input()
        descuento = descuento.replace("%","")
        descuento = int(descuento)
        precioingresar = aplicarDescuento(precio, descuento)
        listacompra.append(precioingresar)
        itera += 1
    for ele in listacompra:
        preciofinal += ele
    totalf = iva(preciofinal)
    return totalf
# funcion main
if(__name__ == "__main__"):
    cantidadArticulos = int(input())
    total = lista(cantidadArticulos)
    print(total)