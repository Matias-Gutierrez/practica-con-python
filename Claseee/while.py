Lista = ["Martin","Marcos","Pedro","Joaquin"]
numeroNombres = len(Lista)
indice = 0
while(indice<numeroNombres):
    print(Lista[indice])
    indice += 1
print("--------------")

numeros = ["7777","9999","222","333","444","555","666","777","888","999","22","33","44","55","66","77","88","99","2","3","4","5","6","7","8","9","0"]
letras = ["s","z","c","f","i","l","o","r","v","y","b","e","h","k","n","q","u","x","a","d","g","j","m","p","t","w"," "]
for nombre in range(len(numeros)):
    if numeros[nombre] == "666":
        print(letras[nombre])
