import matplotlib.pyplot as plt

def lectura(nombre):
    ar = open(nombre)
    fecha = ar.readline()
    fecha = fecha.rstrip('\n')
    X = fecha.split(',')
#   X = ((ar.readline()).rstrip('\n')).split(',')
    XX = list(range(len(X)))
    casos = ar.readline()
    casos = casos.rstrip('\n')
    casos = casos.split(',')
    Y = []
    for elem in casos:
        Y.append(float(elem))
    return X, Y

def graficar(X, Y):
    plt.plot(X, Y)
    plt.show()



def finalizar(X, Y):
    print('Son', len(Y), 'dias' )

if __name__ == "__main__":
    X, Y = lectura('TotalesNacionalesResumen.csv')
    x1, y1 = datos_por_mes(X, Y)
    # graficar(X, Y)
    # finalizar(X, Y)
#   xr, yr = resumen_por mes(X, Y)
