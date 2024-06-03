# UNIDAD 4


def intervalo(): -> None:
    """
    1. Crear una variable con valor 20 va a ser como referencia el minimo.
    Otra con valor de 500, va a ser como referencia el maximo.
    Luego pregunta al usuario por un valor, almacenarlo en otra variable, forzar a que ponga un numero, sino preguntar repetidamente.
    Ese numero transformarlo en integer
    
    Ahora imprimir en pantalla.
    - Si el numero que puso el usuario es menor que el valor minimo definido mostrar el texto VALOR BAJO
    - Si el numero que puso el usuario es mayor que el valor maximo definido mostrar el texto VALOR ALTO
    - Si el numero que puso el usuario esta entre el valor minimo y el valor maximo mostrar el texto VALOR MEDIO
    """
    valor_min = 20
    valor_max = 500

    numero = input("Ingrese un numero: ")
        while not numero.isdigit():
            numero = input("Ingrese un numero: ")

        # debe continuar acá el programa

    print("fin del programa........aun sin resolverlo.")


def es_anio_bisiesto() -> None:
    """
    2. Escriba un programa que pida un año y que escriba si es bisiesto o no.
    Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí.
    """


def contador_bucles() -> None:
    """
    3.
    - Pedir al usuario que ingrese un número de inicio del bucle
    - Pedir al usuario que ingrese un número de fin del bucle
    Validar que el número de inicio sea menor al número de fin, si no es así volver a pedir los dos números, hasta que ésto sea correcto
    Luego de que el usuario ingrese los dos números, mostrar en pantalla todos los números que hay entre el número de inicio y el número de fin
    
    De la siguiente manera:
    
    Este es el bucle número 1
    Este es el bucle número 2
    Este es el bucle número 3
    ---
    Fin del programa.
    """


def promedio_examen() -> None:
    """
    4.Vamos a realizar un programa que nos va a decir la nota promedio de un alumno en todo el cuatrimestre.
    Dentro del cuatrimestre son 4 examenes y luego un examen final.
    La aprobación del cuatrimestre es con nota 6 o mayor de promedio.
    Y si el alumno tiene aprobada la cursada (es decir, obtuvo seis o más de 6 de promedio en sus 4 examenes, rinde el examen final)
    Si el alumno tiene aprobada la cursada y el examen final, entonces el alumno aprobó la materia.
    
    Entonces el programa debe preguntar por la nota de cada examen.
    En función de las respuestas, primero debe avisar el promedio de las 4 notas de los examenes.
    En caso de que el promedio sea mayor o igual a 6, debe avisar que el alumno tiene aprobada la cursada.
    En caso de que el promedio sea menor a 6, debe avisar que el alumno no tiene aprobada la cursada.
    Luego preguntar por nota del final (en caso de que haya aprobado la cursada), si es mayor o igual a 6, debe avisar que el alumno aprobó la materia.
    En caso de que sea menor a 6, debe avisar que el alumno no aprobó el final de la materia, y puede rendir recuperatorio.
    """


def coeficientes_primer_grado() -> None:
    """
    5. Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
    Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los números sean solución. Se recuerda que la fórmula de las soluciones es x = -b / a
    Estos son algunos ejemplos de posibles respuestas (el orden de los ejemplos no tiene por qué corresponder con el orden de las condiciones):

    ECUACIÓN A X + B = 0
    Escriba el valor del coeficiente a: 0
    Escriba el valor del coeficiente b: 3
    La ecuación no tiene solución.

    ECUACIÓN A X + B = 0
    Escriba el valor del coeficiente a: 4.2
    Escriba el valor del coeficiente b: 21
    La ecuación tiene una solución: -5.0

    ECUACIÓN A X + B = 0
    Escriba el valor del coeficiente a: 0
    Escriba el valor del coeficiente b: 0
    Todos los números son solución.
    """


def coeficientes_segundo_grado() -> None:
    """
    6. Escriba un programa que pida los coeficientes de una ecuación de segundo grado (a x² + b x + c = 0) y escriba la solución.
    Se recuerda que una ecuación de segundo grado puede no tener solución, tener una solución única, tener dos soluciones o que todos los números sean solución. Se recuerda que la fórmula de las soluciones cuando hay dos soluciones es x = (-b ± √(b2-4ac) ) / (2a)
    Estos son algunos ejemplos de posibles respuestas (el orden de los ejemplos no tiene por qué corresponder con el orden de las condiciones).

    a	b	c	Solución
    1	-2	2	Sin solución real
    2	-7	3	Dos soluciones: 0.5 y 3.0
    1	2	1	Una solución: -1.0
    0	0	5	Sin solución
    0	0	0	Todos los números son solución
    0	3	2	Una solución: -0.666...
    """


def area_triangulo() -> None:
    """
    7. Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.
    Se recuerda que el área de un triángulo es base por altura dividido por 2 y que el área de un círculo es Pi (aproximadamente 3,141592) por el radio al cuadrado.
    Nota: Utilice como valor de pi el valor 3.141592.
    """


def aproximacion() -> None:
    """9. Escriba un programa que pida tres números y diga si el tercero está más cerca del primero o del segundo."""


def main() -> None:
    print("\nEjercicio 1:\n")
    intervalo()
    print("\nEjercicio 2:\n")
    es_anio_bisiesto()
    print("\nEjercicio 3:\n")
    contador_bucles()
    print("\nEjercicio 4:\n")
    promedio_examen()
    print("\nEjercicio 5:\n")
    coeficientes_primer_grado()
    print("\nEjercicio 6:\n")
    coeficientes_segundo_grado()
    print("\nEjercicio 7:\n")
    area_triangulo()
    print("\nEjercicio 9:\n")
    aproximacion()


if __name__ == "__main__":
    main()