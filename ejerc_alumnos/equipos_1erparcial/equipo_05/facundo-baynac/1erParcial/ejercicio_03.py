from random import randrange

"""
Generar dos funciones diferentes, una que imprima números pares aleatorios y otra que imprima números impares aleatorios
Luego llamar a cada para mostrar en pantalla por un lado 50 números pares y por otro 50 números impares
No usar ni listas, ni diccionarios ni tuplas para resolver el ejercicio
"""


def imprimir_numeros_pares():
    print("Números pares aleatorios: ")
    for x in range(0, 50):
        print(randrange(0, 50, 2))


def imprimir_numeros_impares():
    print("Números impares aleatorios: ")
    for x in range(0, 50):
        print(randrange(1, 50, 2))


imprimir_numeros_pares()
imprimir_numeros_impares()
