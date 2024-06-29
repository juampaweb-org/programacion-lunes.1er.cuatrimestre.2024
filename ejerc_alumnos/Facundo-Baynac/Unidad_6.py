# UNIDAD 6


def calculadora_simple() -> None:
    """1. Calculadora simple: Crea funciones para sumar, restar, multiplicar y dividir dos números enteros o flotantes. Permite al usuario elegir la operación."""


def factorial() -> None:
    """2. Factorial de un número: Escribe una función que calcule el factorial de un número entero dado."""


def numero_primo() -> None:
    """3. Comprobación de número primo: Define una función que verifique si un número entero dado es primo o no."""


def potencia() -> None:
    """4. Cálculo de la potencia de un número: Crea una función que calcule la potencia de un número entero base elevado a una potencia entera."""


def contador_caracteres() -> None:
    """5. Contador de caracteres en una cadena: Escribe una función que tome una cadena como entrada y devuelva el número de caracteres en ella."""


def reversion_cadena() -> None:
    """6. Reversión de cadena: Define una función que invierta una cadena dada."""


def generador_fibonacci() -> None:
    """7. Generador de secuencia Fibonacci: Crea una función que genere los primeros n términos de la secuencia Fibonacci."""


def clave_valor() -> None:
    """8. Generar una función en donde mediante clave valor le pasemos datos de un alumno. Y segun lo que haya pasado imprime una ficha, en caso de que no haya pasado algun valor va a decir sin valor.. Debe poder pasar nombre, apellido, carrera, fecha_nacimiento, email, turno."""


def sumar_multiplicar_nums() -> None:
    """
    9. Realizar una función que reciba n parametros, el primero solamente puede ser o 'sumar' o 'multiplicar', y los siguientes deben ser numeros.
    Si alguno no es un número debe avisar y cortar la ejecución. Y si verifica y son todos los números, debe devolver la suma o multiplicación de los números.
    """    


def verificar_palindromos()-> None:
    """10. Verificador de palíndromos: Crea una función que determine si una cadena dada es un palíndromo o no (es decir, si se lee igual de adelante hacia atrás que de atrás hacia adelante)."""


def main() -> None:
    print("\nEjercicio 1:\n")
    calculadora_simple()
    print("\nEjercicio 2:\n")
    factorial()
    print("\nEjercicio 3:\n")
    numero_primo()
    print("\nEjercicio 4:\n")
    potencia()
    print("\nEjercicio 5:\n")
    contador_caracteres()
    print("\nEjercicio 6:\n")
    reversion_cadena()
    print("\nEjercicio 7:\n")
    generador_fibonacci()
    print("\nEjercicio 8:\n")
    clave_valor()
    print("\nEjercicio 9:\n")
    sumar_multiplicar_nums()
    print("\nEjercicio 10:\n")
    verificar_palindromos()


if __name__ == "__main__":
    main()