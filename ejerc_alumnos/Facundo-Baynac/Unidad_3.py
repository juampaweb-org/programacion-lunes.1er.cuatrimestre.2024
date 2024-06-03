# UNIDAD 3


def imprimir_nombre_edad() -> None:
    """1. Solicita al usuario que ingrese su nombre y su edad. Luego, imprime un mensaje que diga \"¡Hola, `[nombre]`! Tienes `[edad]` años."""


def imprimir_figura() -> None:
    """
    2. Imprima en pantalla las siguientes figuras geometricas (utilizar concatenación y replicación de strings):

    +***************+
    *               *
    *               *
    *               *
    +***************+

    +---+
    |   |
    |   |
    |   |
    +---+

    ###################################
    ###################################
    ##                               ##
    ##                               ##
    ##                               ##
    ###################################
    ###################################
    """


def division_float() -> None:
    """3. Solicita al usuario que ingrese dos números enteros. Luego, convierte estos números a float, realiza la división de ambos y muestra el resultado."""


def sumar_10() -> None:
    """4. Pide al usuario que ingrese una cadena que represente un número entero. Convierte esta cadena a un entero usando la función int() y luego suma 10. Imprime el resultado."""


def mayor_menor_igual() -> None:
    """5. Pregunta al usuario que ingrese un número. Si el número es mayor que 10, imprime "El número es mayor que 10". Si es igual a 10, imprime "El número es igual a 10". De lo contrario, imprime "El número es menor que 10"."""


def mayor_o_menor_edad() -> None:
    """6a. Pregunta al usuario que ingrese su edad. Si la edad es mayor o igual a 18, imprime "Eres mayor de edad". De lo contrario, imprime "Eres menor de edad"."""


def hervor_agua() -> None:
    """6b. Pide al usuario que ingrese una temperatura en Celsius. Si la temperatura es mayor o igual a 100, imprime "El agua está hirviendo". Si es menor o igual a 0, imprime "El agua está congelada". De lo contrario, imprime "El agua está en estado líquido"."""


def numero_positivo_negativo_cero() -> None:
    """7. Pregunta al usuario que ingrese un número. Si es positivo, imprime "El número es positivo". Si es negativo, imprime "El número es negativo". Si es cero, imprime "El número es cero"."""


def dia_de_la_semana() -> None:
    """8. Solicita al usuario que ingrese un número del 1 al 7. Luego, imprime el día de la semana correspondiente (1 para Lunes, 2 para Martes, etc.). Si ingresa un número fuera de ese rango, imprime "Número de día no válido"."""


def main() -> None:
    print("\nEjercicio 1:\n")
    imprimir_nombre_edad()
    print("\nEjercicio 2:\n")
    imprimir_figura()
    print("\nEjercicio 3:\n")
    division_float()
    print("\nEjercicio 4:\n")
    sumar_10()
    print("\nEjercicio 5:\n")
    mayor_menor_igual()
    print("\nEjercicio 6a:\n")
    mayor_o_menor_edad()
    print("\nEjercicio 6b:\n")
    hervor_agua()
    print("\nEjercicio 7:\n")
    numero_positivo_negativo_cero()
    print("\nEjercicio 8:\n")
    dia_de_la_semana()


if __name__ == "__main__":
    main()