#Consigna: 

# Juego de Adivinar el Número Secreto:
# Desarrolla un programa en el que la computadora elija un número aleatorio entre 1 y 100. El usuario deberá intentar adivinar ese número. El programa debe proporcionar pistas, después de cada intento del usuario hasta que adivine correctamente.
# Con respecto a las pistas, si bien está abierto a como quieras resolverlo la idea es ir avisando si está muy alejado, mas o menos alejado, cerca, muy cerca, etc. Pudiendo avisar si el número es mayor o menor al que se intenta adivinar.

import random

def jugar_a_adivinar_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("¡Bienvenido al juego de Adivinar el Número!")
    print("Estoy pensando en un número entre 1 y 100... ¿Podés adivinarlo?")

    while True:
        numero_aleatorio = int(input("¿Qué número creés que estoy pensando? "))
        intentos += 1

        if numero_aleatorio < numero_secreto:
            if numero_secreto - numero_aleatorio > 20:
                print("Muy muy frío... Te diría que intentes con un número un poco más alto.")
            elif numero_secreto - numero_aleatorio > 10:
                print("Frío frío... Intentá con un número un poco más alto.")
            else:
                print("Cerca cerca. Intentá con un número un poco más alto.")
        elif numero_aleatorio > numero_secreto:
            if numero_aleatorio - numero_secreto > 20:
                print("Muy frío... Intentá con un número un poco más bajo.")
            elif numero_aleatorio - numero_secreto > 10:
                print("Frío... Intentá con un número un poco más bajo.")
            else:
                print("Cerca... Intentá con un número un poco más bajo.")
        else:
            print(f"¡Felicidades! ¡Adivinaste el número secreto, el cual fue: {numero_secreto} y solo te tomó {intentos} intentos! :D")
            break

jugar_a_adivinar_el_numero()




# muy buen trabajo
# faltaria controlar con el metodo isdigit() si escribi un numero por que sino dá error en caso de que ingrese una letra..
