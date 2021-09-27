i = 0
contador = 0
aux = 20 
while (i<20):
    modulo=i%3
    if (modulo==1):
        i=i+3
    elif modulo==2: 
        i=i-4
    else:
        i=i+5
    contador=contador+1
print(i)
print(aux)
