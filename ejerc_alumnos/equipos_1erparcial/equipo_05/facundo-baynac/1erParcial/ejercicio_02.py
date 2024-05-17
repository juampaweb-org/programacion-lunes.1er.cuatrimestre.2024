"""
Crear una función que reciba la calificación de un estudiante como parámetro, y su nombre
Determinar y devolver la letra equivalente a la calificación:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: < 60

Imprimir la calificación original, la letra correspondiente y su nombre.
La función debe devolver un string con lo expresado anteriormente.

Ejemplo:
calificacion(95, "Juan") -> "La calificación de Juan es 95, su letra es A"
calificacion(60, "Maria") -> "La calificación de Maria es 60, su letra es D"
"""


def calificacion_estudiante(nombre, calificacion):
    if calificacion >= 90:
        return "La calificación de " + nombre + " es " + str(calificacion) + ", su letra es A"
    elif calificacion >= 80:
        return "La calificación de " + nombre + " es " + str(calificacion) + ", su letra es B"
    elif calificacion >= 70:
        return "La calificación de " + nombre + " es " + str(calificacion) + ", su letra es C"
    elif calificacion >= 60:
        return "La calificación de " + nombre + " es " + str(calificacion) + ", su letra es D"
    else:
        return "La calificación de " + nombre + " es " + str(calificacion) + ", su letra es F"


print("Ingrese el nombre del estudiante: ")
estudiante = str(input())
print("Ingrese la calificacion: ")
calificacion = int(input())
print(calificacion_estudiante(estudiante, calificacion))
