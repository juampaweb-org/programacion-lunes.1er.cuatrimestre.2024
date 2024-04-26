# Nos tocó resolver el Ejercicio 6 y de la Unidad 5 los (Script 3 y 7) 
# Saludos

# Ejercicio 6

# Escriba un programa que pida los coeficientes de una ecuación de segundo grado (a x² + b x + c = 0) y escriba la solución.

# Se recuerda que una ecuación de segundo grado puede no tener solución, tener una solución única, tener dos soluciones o que todos los números sean solución. Se recuerda que la fórmula de las soluciones cuando hay dos soluciones es x = (-b ± √(b2-4ac) ) / (2a)

# Estos son algunos ejemplos de posibles respuestas (el orden de los ejemplos no tiene por qué corresponder con el orden de las condiciones).


# a b c Solución
# 1 -2 2 Sin solución real
# 2 -7 3 Dos soluciones: 0.5 y 3.0
# 1 2 1 Una solución: -1.0
# 0 0 5 Sin solución
# 0 0 0 Todos los números son solución
# 0 3 2 Una solución: -0.666...



# Programa para resolver ecuaciones de segundo grado

import math  # Importamos la funcion Math para realizar la función matematica de la raiz cuadrada

# Se solicitan los coeficientes a, b y c al usuario
a = float(input("Ingrese el coeficiente a: ")) # Se almacenan los datos ingresados en cada variables de los coeficientes para convertirlos a numero
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

# Se calcula el discriminante
discriminante = b**2 - 4 * a * c # El Valor del determinante nos dice cuantas soluciones tiene la ecuación

# Se analizan los posibles casos
if discriminante > 0: # Si el discriminantes es mayor a cero la ecuación tiene dos soluciones reales y se calcula usando la ecuación de segundo grado
    # La ecuación tiene dos soluciones reales
    x1 = (-b + math.sqrt(discriminante)) / (2 * a)
    x2 = (-b - math.sqrt(discriminante)) / (2 * a)
    print("Las soluciones son:", x1, x2)
elif discriminante == 0: # Si el discriminante es igual a cero la ecuación tiene una solución real y se calcula usando la misma formula pero simplificando la expresión
    # La ecuación tiene una solución real
    x = -b / (2 * a)
    print("La solución es:", x)
else:
    # La ecuación no tiene soluciones reales
    print("La ecuación no tiene soluciones reales.") # Si es discriminante es menor que cero la ecuación no tiene soluciones reales y se muestra el mensaje


exit()





# +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Contador de Caracteres Especificos: Script 07
# Crea un programa que solicite al usuario ingresar una letra o carácter. El programa debe contar y mostrar cuántas veces aparece ese carácter en una frase dada. El procedimiento es el siguiente:
# Pide al usuario que ingrese una frase.
# Luego, pide al usuario que ingrese un carácter para buscar en la frase.
# Utiliza un bucle for junto con índices para recorrer la frase y contar las ocurrencias del carácter especificado.
# Muestra el número total de veces que aparece ese carácter en la frase.
# Solicitar al usuario que ingrese una frase
frase = input(" Por favor ingrese una frase: ") # La frase ingresada se guarda en la variable frase con la funcion input

# Solicitar al usuario que ingrese un carácter para buscar en la frase
caracter_a_buscar = input("Por favor ingrese un carácter para buscar en la frase: ") # El caracter ingresado se guarda en la variable caracter_a_buscar con la funcion input

# Inicializar el contador de ocurrencias del carácter
contador = 0 # En la variable contador vamos a guardar la cantidad de veces del carater a buscar en la frase inicializandolo desde cero

# Utilizar un bucle for junto con índices para recorrer la frase y contar las ocurrencias del carácter especificado
for letra in frase: # Usamos for para crear un Bucle que recorra cada letra de la frase
    if letra == caracter_a_buscar: # En cada recorrido del Bucle se verifica si la letra (letra) es igual al caracter que se esta buscando en (caracter_a_buscar)
        contador += 1 # Incremento del contador

# Mostrar el número total de veces que aparece ese carácter en la frase
print(f"El carácter '{caracter_a_buscar}' aparece {contador} veces en la frase.") # Al finalizar de recorrer toda la frase muestra un mensaje que nos indica cuantas veces aparece el caracter de busqueda en la frase de la variable caracter_a_buscar y contador con la cantidad de veces


# +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Calculadora de Propina: Script 03
# Desarrolla una calculadora de propinas que solicite al usuario ingresar el total de la cuenta en un restaurante. El programa debe calcular automáticamente diferentes opciones de propinas
# (por ejemplo, 15%, 18%, 20%) y mostrar el monto total a pagar incluyendo la propina

# Solicitar al usuario que ingrese el total de la cuenta en el restaurante
total_cuenta = float(input("Ingresa el total de la cuenta en el restaurante: ")) # Ingresamos el total de la cuenta usando float para ingresar un numero se almacena en total_cuenta

# Definir las opciones de propina
opciones_propina = [15, 18, 20] # Creamos una lista opciones_propina y le asignamos valores que van a ser los porcentajes

# Calcular y mostrar diferentes opciones de propinas
print("\nOpciones de propina:") # Muestra un mensaje
for porcentaje in opciones_propina: # Este Bucle for recorre la lista opciones_propina de a uno por uno va haciendo los calculos
    propina = total_cuenta * (porcentaje / 100) # Hace la cuenta del total por cada porcentaje y divide por 100 y almaceno en propina
    total_con_propina = total_cuenta + propina # total a paga incluida la propina almaceno el valor en total_con_propina

    # Mostrar el resultado para cada opción de propina
    print(f"\nPropina del {porcentaje}%:") # Muestra el porcentaje de la propina a pagar
    print(f"Propina: ${propina:.2f}") # Muestra el valor de la propina que corresponde al porcentaje anterior :.2f muestra dos decimales luego del punto
    print(f"Total a pagar incluyendo la propina: ${total_con_propina:.2f}") # Muestra el total a pagar incluida la propina

# +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






## el primero me dá lo siguiente:
# (.venv)  infra/programacion-lunes.1er.cuatrimestre.2024 $ /var/www/html/utils/.venv/bin/python /var/www/html/istea/infra/programacion-lunes.1er.cuatrimestre.2024/ejerc_alumnos/equipos_1erparcial/equipo_04/resueltos.py
# Ingrese el coeficiente a: 3
# Ingrese el coeficiente b: 4
# Ingrese el coeficiente c: 5
# La ecuación no tiene soluciones reales.


## controlar todos y avisarme... Separarlos en diferentes scripts que indiquen arriba el enunciado comentado el texto.