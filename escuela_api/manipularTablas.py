ruta_archivo = "../datos/estudiante.csv"

with open(ruta_archivo, 'r') as archivo:
    next(archivo, None)
    for linea in archivo:
        linea=linea.rstrip()
        lista = linea.split(",") 
        print(lista[1])



