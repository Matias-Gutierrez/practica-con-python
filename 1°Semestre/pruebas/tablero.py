import random
# Función movimiento alfil
def mov_alfi(x_alfil, y_alfil):
    cuadrante = random.randint(1,4)
    casillas = random.randint(1,(x_tablero-1))
    Contador = 1
    x_alfilc= x_alfil
    y_alfilc= y_alfil
    c=0
    # tablero[x_alfil][y_alfil]="*"
    if cuadrante == 1:
        Contador = 1
        while Contador < casillas:
            x_alfil = x_alfil + 1
            y_alfil = y_alfil + 1
            if (((x_alfil > x_tablero-1) or (x_alfil < 0)) or ((y_alfil > y_tablero-1) or (y_alfil < 0))):
                x_alfil -= Contador
                y_alfil -= Contador
                Contador= casillas
            elif (tablero[x_alfil][y_alfil]== "T"):
                x_alfil -= Contador
                y_alfil -= Contador
                Contador= casillas
            Contador +=1
            
    elif cuadrante == 2:
        Contador = 1
        while Contador < casillas:
            x_alfil -= 1
            y_alfil += 1
            if (((x_alfil > x_tablero-1) or (x_alfil < 0)) or ((y_alfil > y_tablero-1) or (y_alfil < 0))):
                x_alfil += Contador
                y_alfil -= Contador
                Contador= casillas
            elif (tablero[x_alfil][y_alfil]== "T"):
                x_alfil += Contador
                y_alfil -= Contador
                Contador= casillas
            Contador += 1
        
    elif cuadrante == 3:
        Contador = 1
        while Contador < casillas:
            x_alfil -= 1
            y_alfil -= 1
            if (((x_alfil > x_tablero-1) or (x_alfil < 0)) or ((y_alfil > y_tablero-1) or (y_alfil < 0))):
                print(Contador)
                x_alfil += Contador
                y_alfil += Contador
                Contador= casillas
            elif (tablero[x_alfil][y_alfil]== "T"):
                x_alfil += Contador
                y_alfil += Contador
                Contador = casillas
            Contador+=1
    elif cuadrante == 4:
        Contador = 1
        while Contador < casillas:
            x_alfil += 1
            y_alfil -= 1

            if (((x_alfil > x_tablero-1) or (x_alfil < 0)) or ((y_alfil > y_tablero-1) or (y_alfil < 0))):
                x_alfil -= Contador
                y_alfil += Contador
                Contador= casillas
            
            elif (tablero[x_alfil][y_alfil]== "T"):
                x_alfil -= Contador
                y_alfil += Contador
                Contador = casillas
            Contador += 1
    if tablero[x_alfil][y_alfil] == "C":
        c = 1
    tablero[x_alfilc][y_alfilc]="*"
    tablero[x_alfil][y_alfil]="A"
    return (x_alfil,y_alfil,c)

# Función movimiento torre

# Juego

# Solicitud dimensiones del tablero
print("Escriva la la dimension del tablero e formato X,Y")
dimensiones = input().split(",")
x_tablero = int(dimensiones[0])
y_tablero = int(dimensiones[1]) 

# Creacion de la matriz 
tablero=[[0] * y_tablero for i in range(x_tablero)]
for i in range(x_tablero):
    for j in range(y_tablero):
        tablero[i][j] = "*"

# Asignación posiciones de las piezas y trofeo
tablero[0][0] = "A"
tablero[x_tablero-1][y_tablero-1] = "A"
tablero[0][y_tablero-1] = "T"
tablero[x_tablero-1][0] = "T"
tablero[(x_tablero//2)][(y_tablero//2)] = "C"
fin = "no"
x_alfil1 = 0
y_alfil1 = 0
x_alfil2 = x_tablero-1
y_alfil2 = y_tablero-1

resul = ""
jugadas = 1
for row in tablero:
        print(' '.join([str(elem) for elem in row]))

while fin == "no":
    print(f"Ronda {jugadas}")
    print()
    tablero[x_alfil1][y_alfil1]="*"
    a = mov_alfi(x_alfil1,y_alfil1)
    x_alfin1 = a[0]
    y_alfil1 = a[1]
    tablero[x_alfil2][y_alfil2]="*"
    b = mov_alfi(x_alfil2,y_alfil2)
    x_alfil2 = b[0]
    y_alfil2 = b[1]
    if a[2] == 1 or b[2]==1:
        fin = "si"
        resul="Perdiste"
    for row in tablero:
        print(' '.join([str(elem) for elem in row]))
    print()
    jugadas += 1
    input("Escribe algo: ")
print(f"Juego finalizado, {resul}")