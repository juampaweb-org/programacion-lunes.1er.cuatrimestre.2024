# UNIDAD 7


def lista_numeros() -> None:
    """1. Escribe un programa que solicite al usuario ingresar 5 números enteros y los almacene en una lista. Luego, imprime la lista resultante."""


def lista_companieros() -> None:
    """2. Crea una lista con los nombres de tus compañeros de clase. Imprime la lista y luego ordena los nombres en orden alfabético. Imprime la lista nuevamente para verificar el orden."""


def lista_num_pares() -> None:
    """3. Escribe una función que genere una lista de los primeros 10 números pares y luego imprima la lista. A dicha función le vamos a pasar como parámetro una lista de numeros. Esta es la lista que debe controlar para reotrnarnos una nueva lista con solamente los primero diez numeros paares que encuentre."""


def lista_csv() -> None:
    """4. Desarrolla un programa que pida al usuario ingresar una lista de palabras separadas por comas. Luego, convierte esta cadena en una lista y la imprime."""


def lista_potencia_cuadrada() -> None:
    """5. Crea una lista con los números del 1 al 10. Utiliza un bucle para elevar cada número al cuadrado y almacenar el resultado en una nueva lista. Imprime la lista de cuadrados resultante."""


def del_duplicados_lista() -> None:
    """6. Escribe un programa que elimine todos los elementos duplicados de una lista y luego imprima la lista sin duplicados."""


def busca_elemento_en_lista() -> None:
    """
    7a. Busca un elemento: Crea una función que busque un elemento específico dentro de una lista y devuelva su índice o un mensaje si no lo encuentra.
    Ejemplo: [1, 2, 3, 4, 5], buscando el elemento 3, devuelve 2.
    """


def extrae_sublista() -> None:
    """
    7b. Extrae una sublista: Escribe un programa que extraiga una sublista de una lista principal, especificando el índice inicial y el final (o la longitud de la sublista).
    Ejemplo: [1, 2, 3, 4, 5, 6], extrayendo desde el índice 2 hasta el final, devuelve [3, 4, 5, 6].
    """


def invierte_lista() -> None:
    """
    1. Invierte una lista: Escribe un programa que invierta el orden de los elementos de una lista.
    Ejemplo: [1, 2, 3, 4, 5] se convierte en [5, 4, 3, 2, 1].
    Primero resolvelo manualmente. Luego, crea una función que lo haga automáticamente (Ac+a podés usar 100 numeros)
    """


def elimina_duplicados() -> None:
    """
    2. Elimina duplicados: Crea una función que elimine los elementos duplicados de una lista.
    Ejemplo: [1, 2, 3, 1, 2, 4] se convierte en [1, 2, 3, 4].
    """


def combina_dos_listas() -> None:
    """
    3. Combina dos listas: Escribe una función que combine dos listas en una sola lista.
    Ejemplo: [1, 2, 3] y [4, 5, 6] se convierte en [1, 2, 3, 4, 5, 6].
    """


def intersec_dif_conjuntos() -> None:
    """
    4a. Intersección y diferencia de conjuntos:
    Crea dos funciones: una que calcule la intersección (elementos comunes) y otra que calcule la diferencia (elementos exclusivos) entre dos listas. Las funciones deben poder trabajar con listas de cualquier longitud y tipo de elemento.
    """


def lista_rangos() -> None:
    """
    4b. Creación de una lista a partir de un rango:
    Escribe una función que genere una lista a partir de un rango de números especificado por el usuario. La función debe permitir definir el valor inicial, el valor final y el incremento (paso) entre los elementos. La lista generada debe contener todos los números dentro del rango especificado.
    """


def busqueda_en_lista() -> None:
    """
    5. Búsqueda en una lista:
    Implementa la búsqueda en una lista de números. La función debe recibir como parámetros la lista ordenada y el elemento a buscar. La función debe devolver el índice del elemento en la lista si lo encuentra, o un mensaje indicando que el elemento no está presente.
    No debemos utilizar las funciones index() ni find() de Python. Debemos hacer la búsqueda manualmente.
    """


def main() -> None:
    print("\n--- NIVEL SIMPLE ---\n\nEjercicio 1:\n")
    lista_numeros()
    print("\nEjercicio 2:\n")
    lista_companieros()
    print("\nEjercicio 3:\n")
    lista_num_pares()
    print("\nEjercicio 4:\n")
    lista_csv()
    print("\nEjercicio 5:\n")
    lista_potencia_cuadrada()
    print("\nEjercicio 6:\n")
    del_duplicados_lista()
    print("\nEjercicio 7a:\n")
    busca_elemento_en_lista()
    print("\nEjercicio 7b:\n")
    extrae_sublista()
    print("\n--- NIVEL MEDIO ---\n\nEjercicio 1:\n")
    invierte_lista()
    print("\nEjercicio 2:\n")
    elimina_duplicados()
    print("\nEjercicio 3:\n")
    combina_dos_listas()
    print("\nEjercicio 4a:\n")
    intersec_dif_conjuntos()
    print("\nEjercicio 4b:\n")
    lista_rangos()
    print("\nEjercicio 5:\n")
    busqueda_en_lista()


if __name__ == "__main__":
    main()