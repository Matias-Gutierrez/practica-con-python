primer = float(input("Puntaje del primer jugador: "))
segundo = float(input("Puntaje del segundo jugador: "))
if primer < segundo:
    print("el ganador es el segundo jugador")
elif primer > segundo :
    print("El ganador es el primer jugador")
else:
    print("Hay un empate")