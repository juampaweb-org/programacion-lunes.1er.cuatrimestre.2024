# Unidad 4 - Ejercicio 2

# Solicitar al usuario que ingrese un año
año = int(input("Por favor, ingrese un año: "))

# Verificar si el año es bisiesto e imprimir el resultado
# Un año es bisiesto si es divisible por 4 pero no por 100,
# a menos que sea divisible por 400.

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")




# buen trabajo!

# fijense esa forma de escribir print que pusieron en la línea 11 y 13
# es una forma de concatenar strings con variables, se llama f-string
# la vamos a ver por que se utiliza mucho