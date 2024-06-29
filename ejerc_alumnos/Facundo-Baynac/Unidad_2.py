# UNIDAD 2


import math  # Para ejercicio 4


def area_rectangulo() -> None:
    """Calcula el área de un rectángulo con base 5 y altura 3. Imprime el resultado."""
    altura_rectangulo = 3
    base_rectangulo = 5
    area = altura_rectangulo * base_rectangulo
    print(f"El área de un rectángulo con base 5 y altura 3 es: {area}")


def convierte_temperatura() -> None:
    """Convierte la temperatura de Celsius a Fahrenheit. Pide al usuario ingresar la temperatura en Celsius y
    luego imprime la temperatura equivalente en Fahrenheit."""
    print("Ingrese la temperatura en Celsius:")
    temperatura_celsius = input()
    temperatura_celsius = int(temperatura_celsius)
    temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32
    print(f"La temperatura en Fahrenheit es: {temperatura_fahrenheit}")


def concat_string() -> None:
    """Concatena tu nombre y tu edad como strings y guárdalos en una variable. Luego imprime el tipo de dato
    de esa variable."""
    nombre = "Facundo"
    edad = "23"
    nombre_y_edad = nombre + edad
    print(f"El tipo de dato de la variable nombre_y_edad es: {type(nombre_y_edad)}")


def calcular_area_circulo() -> None:
    """Calcula el área de un círculo con radio 4. Imprime el resultado."""
    radio_circulo = 4
    area_circulo = math.pi * radio_circulo ** 2
    print(f"El área de un círculo con radio 4 es: {area_circulo}")


def calculadora() -> None:
    """Pide al usuario que ingrese dos números y muestra la suma, resta, multiplicación y división de esos números."""
    print("Ingrese un número:")
    numero1: int = int(input())  # pasamos del tipo string a int para poder operar
    print("Ingrese otro número:")
    numero2: int = int(input())  # pasamos del tipo string a int para poder operar
    suma = int(numero1) + int(numero2)
    print("suma: " + str(suma))
    resta = numero1 - numero2
    print("resta: " + str(resta))
    multiplicacion = numero1 * numero2
    print("multiplicación: " + str(multiplicacion))
    if numero2 != 0:
        division = numero1 / numero2
        print("división: " + str(division))  # se necesita exceptuar el caso de division por cero
    else:
        print("No se puede dividir por 0.")


def operacion_compleja() -> None:
    """Almacena el resultado de una operación aritmética compleja en una variable y luego imprime tanto el resultado
    como el tipo de dato de esa variable."""
    resultado_operacion = 2 * 4 / 3 + 4
    print(f"El resultado de la operación (2 * 4 / 3 + 4) es: {resultado_operacion}"
          f",y de tipo: {type(resultado_operacion)}")


def aprobo_desaprobo() -> None:
    """Crea una variable booleana que represente si un alumno ha aprobado o no un examen y luego imprime su estado."""
    aprobado: bool = False
    print(f"Estado de la variable booleana aprobado: {aprobado}")


def calcular_perimetro_triangulo() -> None:
    """Calcula el perímetro de un triángulo equilátero con lados de longitud 6. Imprime el resultado."""
    longitud_lado = 6
    perimetro_triangulo = 3 * longitud_lado
    print(f"El perímetro del triángulo equilátero es: {perimetro_triangulo}")


def imprime_tipo_de_dato() -> None:
    """Pide al usuario que ingrese su nombre, edad y ciudad de residencia y luego imprime cada uno de esos datos con su respectivo tipo de dato."""
    print("Ingrese nombre:\n")
    nombre = input()
    print("Ingrese edad:\n")
    edad = int(input()) # Input siempre lo toma como string pero debería ser integer
    print("Ingrese ciudad de residencia: \n")
    ciudad = input()
    print(f"Tipo de dato nombre: {str(type(nombre))} \nTipo de dato edad: {str(type(edad))} \nTipo de dato ciudad: {str(type(ciudad))}")


def operacion_matematica() -> None:
    """Realiza una operación matemática que involucre paréntesis, multiplicación, suma y resta. Guarda el resultado en una variable y luego imprímela junto con su tipo de dato."""
    resultado = (14 * 34) / 12 * (2 - 3 + 6)
    print(f"El resultado es: {str(resultado)} y su tipo de dato es: {str(type(resultado))}")


def main() -> None:
    print("\nEjercicio 1:\n")
    area_rectangulo()
    print("\nEjercicio 2:\n")
    convierte_temperatura()
    print("\nEjercicio 3:\n")
    concat_string()
    print("\nEjercicio 4:\n")
    calcular_area_circulo()
    print("\nEjercicio 5:\n")
    calculadora()
    print("\nEjercicio 6:\n")
    operacion_compleja()
    print("\nEjercicio 7:\n")
    aprobo_desaprobo()
    print("\nEjercicio 8:\n")
    calcular_perimetro_triangulo()
    print("\nEjercicio 9:\n")
    imprime_tipo_de_dato()
    print("\nEjercicio 10:\n")
    operacion_matematica()


if __name__ == "__main__":
    main()