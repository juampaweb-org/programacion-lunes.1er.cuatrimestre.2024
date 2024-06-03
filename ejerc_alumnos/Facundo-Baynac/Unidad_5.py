# UNIDAD 5


def juego_adivinar_numero() -> None:
    """
    1. Juego de Adivinar el Número Secreto:
    Desarrolla un programa en el que la computadora elija un número aleatorio entre 1 y 100. El usuario deberá intentar adivinar ese número. El programa debe proporcionar pistas, después de cada intento del usuario hasta que adivine correctamente.
    Con respecto a las pistas, si bien está abierto a como quieras resolverlo la idea es ir avisando si está muy alejado, mas o menos alejado, cerca, muy cerca, etc. Pudiendo avisar si el número es mayor o menor al que se intenta adivinar.
    """


def tareas_pendientes() -> None:
    """
    2. Lista de Tareas Pendientes:
    Crea un programa que permita al usuario mantener una lista de tareas pendientes. El programa debe permitir agregar tareas nuevas, marcar tareas como completadas y mostrar la lista actualizada de tareas.
    """


def calculadora_propina() -> None:
    """
    3. Calculadora de Propina:
    Desarrolla una calculadora de propinas que solicite al usuario ingresar el total de la cuenta en un restaurante. El programa debe calcular automáticamente diferentes opciones de propinas (por ejemplo, 15%, 18%, 20%) y mostrar el monto total a pagar incluyendo la propina.
    """


def carrera_autos() -> None:
    """ 
    4. Simulador de Carrera de Autos:
    Implementa un programa que simule una carrera de autos entre varios competidores. Cada competidor tiene una velocidad aleatoria y la carrera se desarrolla en rondas. El programa debe mostrar el progreso de la carrera en cada ronda y determinar el ganador al final.
    """


def gestor_inventario() -> None:
    """
    5. Gestor de Inventario de Tienda:
    Crea un sistema simple de gestión de inventario para una tienda. El programa debe permitir agregar productos nuevos, actualizar la cantidad disponible de un producto y mostrar la lista actualizada de productos en stock.
    """


def area_perimetro_figuras() -> None:
    """
    6. Crea un programa que permita al usuario calcular el área y el perímetro de varias figuras geométricas. El programa debe presentar un menú con las siguientes opciones:

    Calcular el área y el perímetro de un círculo.
    Calcular el área y el perímetro de un cuadrado.
    Calcular el área y el perímetro de un triángulo.
    Salir del programa.
    
    Área y Perímetro de un Círculo:
    - Área del círculo: Área = π × radio²
    - Perímetro del círculo: Perímetro = 2 × π × radio
    Área y Perímetro de un Cuadrado:
    - Área del cuadrado: Área = lado²
    - Perímetro del cuadrado: Perímetro = 4 × lado
    Área y Perímetro de un Triángulo:
    - Área del triángulo: Área = 0.5 × base × altura
    - Perímetro del triángulo: Suma de los 3 lados
    """


def contador_carac_esp() -> None:
    """
    7. Contador de Caracteres Específicos:
    - Crea un programa que solicite al usuario ingresar una letra o carácter. El programa debe contar y mostrar cuántas veces aparece ese carácter en una frase dada. El procedimiento es el siguiente:
    - Pide al usuario que ingrese una frase.
    - Luego, pide al usuario que ingrese un carácter para buscar en la frase.
    - Utiliza un bucle for junto con índices para recorrer la frase y contar las ocurrencias del carácter especificado.
    - Muestra el número total de veces que aparece ese carácter en la frase.
    """


def detector_palindromos() -> None:
    """
    8. Detector de Palíndromos:
    - Desarrolla un programa que verifique si una palabra ingresada por el usuario es un palíndromo (una palabra que se lee igual de adelante hacia atrás). El proceso es el siguiente:
    - Pide al usuario que ingrese una palabra.
    - Utiliza un bucle for junto con índices para recorrer la mitad del string y comparar los caracteres desde el principio con los caracteres desde el final.
    - Si todos los caracteres coinciden, indica que la palabra es un palíndromo; de lo contrario, indica lo contrario.
    """


def main() -> None:
    print("\nEjercicio 1:\n")
    juego_adivinar_numero()
    print("\nEjercicio 2:\n")
    tareas_pendientes()
    print("\nEjercicio 3:\n")
    calculadora_propina()
    print("\nEjercicio 4:\n")
    carrera_autos()
    print("\nEjercicio 5:\n")
    gestor_inventario()
    print("\nEjercicio 6:\n")
    area_perimetro_figuras()
    print("\nEjercicio 7:\n")
    contador_carac_esp()
    print("\nEjercicio 8:\n")
    detector_palindromos()


if __name__ == "__main__":
    main()