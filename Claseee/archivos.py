archivo = open('nombres.txt')
total_lines = sum(1 for line in archivo)
arch = open('nombres.txt')
for __elem__ in range(total_lines):
    print( (arch.readline()).strip("\n"))
arch.close()
archivo.close()