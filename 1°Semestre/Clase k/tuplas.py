#Creamos la lista llamada "Array"
Array = []

#Usamos la funcion append para ingresar un valor al final de la lista
Array.append("Lissette")
Array.append("Francisco")

#Usamos la funcion insert(posicion, valor) donde posicion es la posicion en donde ingresaremos el dato y valor es el dato a ingresar
Array.insert(2, "Matias")

#Usamos la funcion extend para ingresar mas de un valor al final de la lista
Array.extend(["Javier","Carolina","Alejandro"])

print(Array)
#Para borrar el dato de la ultima posicion de la lista
Array.pop()

print(Array)
#Para borrar el dato de una posicion exacta se usa pop(posicion)
#donde posicion se remplaza por la posicion del dato a eliminar
Array.pop(3)
Array.pop(3)

#Para borrar exactamente un dato se usa remove(dato)
#donde dato se remplaza por el dato a borrar
Array.remove("Matias")

#Invertir el orden de la lista
Array.reverse()

#Ordenar los datos de la tupla de manera ascendente 
Array.sort()

#Ordenar los datos de la tupla de manera descendente
Array.sort(reverse=True)

#Para contar cuantas veces esta algun dato en la lista se usa count(dato)
#donde dato lo remplazamos por el dato a buscar
print(Array.count("Francisco"))

#Para encontrar en que posicion se encuentra un dato usamos la funcion index(dato)
#donde dato lo remplazamos por el dato a buscar la posicion
print(Array.index("Lissette"))

print(Array)

#Para concatenar dos listas usamos la siguiente sintaxis
Array2 = Array + Array
print(Array2)

