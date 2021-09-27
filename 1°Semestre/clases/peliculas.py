pelicula1 = int(input())
pelicula2 = int(input())
pelicula3 = int(input())
prime = input()

if pelicula1>pelicula2 and pelicula1>pelicula3:
    pagar=pelicula2+pelicula3
    descuento=(pelicula2+pelicula3)*0.2

if pelicula2>pelicula1 and pelicula1>pelicula3:
    pagar=pelicula1+pelicula3
    descuento=(pelicula1+pelicula3)*0.2

if pelicula3>pelicula1 and pelicula1>pelicula2:
    pagar=pelicula2+pelicula1
    descuento=(pelicula2+pelicula1)*0.2

if prime.title() == "Si":
    print("El total a pagar por la promocion mas el decuento por el prime es $",(pagar-descuento))
else:
    print("El total a pagar por la promo es $",pagar)