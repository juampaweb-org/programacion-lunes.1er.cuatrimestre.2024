# Utilizar pi desde el modulo math de Python
import math


def calcular_area_circulo(radio_circulo) -> None:
    """Calcula el área del círculo según el radio dado"""
    area_circulo = radio_circulo * math.pi ** 2
    print("El área del círculo es: " + str(area_circulo))


def calcular_area_triangulo(base_triangulo, altura_triangulo) -> None:
    """Calcula el área del triangulo según la base y la altura dada"""
    area_triangulo = base_triangulo * altura_triangulo / 2
    print("El área del triángulo es: " + str(area_triangulo))


def calcular_area_cuadrado(lado_cuadrado) -> None:
    """Calcula el área del cuadrado según un lado"""
    area_cuadrado = lado_cuadrado ** 2
    print("El área del cuadrado es: " + str(area_cuadrado))


def main() -> None:
    """Pregunta si se quiere calcular el área de un triángulo, la de un círculo o la de un cuadrado y la calcula"""
    print("Quiere calcular el área de un triángulo(T), la de un círculo(C) o la de un cuadrado(U)"
          "\nIngrese la letra T - C - U: ")
    opcion_elegida = input()

    if opcion_elegida == "c" or opcion_elegida == "C":
        print("\nIngrese el radio del círculo que quiere calcular: ")
        calcular_area_circulo(int(input()))
    elif opcion_elegida == "t" or opcion_elegida == "T":
        print("\nIngrese la base del triángulo que quiere calcular: ")
        base_triangulo = int(input())
        print("\nIngrese la altura del triángulo que quiere calcular: ")
        altura_triangulo = int(input())
        calcular_area_triangulo(base_triangulo, altura_triangulo)
    elif opcion_elegida == "u" or opcion_elegida == "U":
        print("\nIngrese el largo de un lado del cuadrado: ")
        lado_cuadrado = int(input())
        calcular_area_cuadrado(lado_cuadrado)
    else:
        print("\nUsted ingresó un valor incorrecto.\n")


if __name__ == "__main__":
    main()
