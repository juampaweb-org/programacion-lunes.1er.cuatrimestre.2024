


# Ruta absoluta
# C:\Users\Usuario\Documents\Python\unidad-11\en_clase\02-archivos_comenzamos.py


# Archivos en Windows
# Ruta absoluta
# C:\Users\Usuario\Documents\Python\unidad-11\en_clase\02-archivos_comenzamos.py


# Ruta relativa en LINUX
# en_clase/02-archivos_comenzamos.py

# Ruta Absoluta en LINUX
# /home/usuario/Documentos/Python/unidad-11/en_clase/02-archivos_comenzamos.py


directorio = '/var/www/html/istea/infra/programacion-lunes.1er.cuatrimestre.2024/archivos/'

nombre_archivo = 'archivo_pepe.txt'
nombre_archivo_dos = 'archivo_pepe_dos.txt'
# ruta_completa = directorio + nombre_archivo


try:
    archivo = open( directorio + 'archivo_pepe.txt', 'r')
    print(archivo.read())
    archivo.close()

except:
    print("Por alguna razón no se pudo abrir el archivo....")




print("Continua por acá el programa......")
