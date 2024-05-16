def promedio_notas(nombre, lista_notas) -> str:
    """
    Resuelve el promedio de todas las notas y retorna un string indicando la cantidad de notas que se promediaron,
    y los valores.

    Args:
        nombre (str): nombre del alumno
        lista_notas (list): lista de notas del alumno

    Returns:
        str: cantidad de notas que se promediaron, y los valores
    """
    total_notas: int = 0
    for i in range(len(lista_notas)):
        total_notas = total_notas + int(lista_notas[i])
    promedio = total_notas / len(lista_notas)
    return (f"Se están promediando {len(lista_notas)} notas con valores de {lista_notas[0:len(lista_notas)]}"
            f"\nEl promedio de {nombre} es {promedio:.2f}")


def main() -> None:
    """
    Pide al usuario el nombre del alumno y las notas a promediar, luego llama a la función promedio_notas para
    calcular el promedio e imprime por pantalla el resultado.

    La salida por pantalla es ser asi:

    Se están promediando 3 notas, con valores de (8, 9, 7)
    El promedio de Federico es 8.3
    """
    print("Escriba el nombre del alumno: ")
    alumno = input()

    continuar = "s"
    notas = []

    while continuar == 's' or continuar == 'S':
        print("Escriba una nota: ")
        notas.append(input())
        print("Desea continuar operando? s/n: ")
        continuar = input()
    print(promedio_notas(alumno, notas))
