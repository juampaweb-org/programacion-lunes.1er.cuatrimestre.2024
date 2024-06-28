

archivo = 'temperaturas.txt'

try:

    with open(archivo, 'r') as stream_archivo:
        for linea in stream_archivo.readlines():
            print(linea)


except:
    print("Por algún motivo, no se pudo abrir el archivo....")



