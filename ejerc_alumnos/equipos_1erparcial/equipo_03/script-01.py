# Juego de Adivinar el Número Secreto:
# Desarrolla un programa en el que la computadora elija un número aleatorio entre 1 y 100. El usuario deberá intentar adivinar ese número. 
# El programa debe proporcionar pistas, después de cada intento del usuario hasta que adivine correctamente.
# Con respecto a las pistas, si bien está abierto a como quieras resolverlo la idea es ir avisando si está muy alejado,
# mas o menos alejado, cerca, muy cerca, etc. Pudiendo avisar si el número es mayor o menor al que se intenta adivinar.

import random

cantidadvidas=int(10)
numerosecreto=int(random.randint(0,100))
numerousuario=int(0)
findeljuego="NO"
#while numerosecreto!=numerousuario:   Podria utilizarlo, Pero le agrego el apartado de vidas, tambien podria utilizar not(numerosecreto==numerousuario or cantidadvidas==0)  not(false or false)=true
while findeljuego=="NO":
    print(f"Te quedan {cantidadvidas} vidas")
    numerousuario=int(input("Ingresa el numero que creas correcto entre 0 y 100: "))
    distanciaentrenumeros=abs(numerosecreto-numerousuario)
    #print("Depuracion variable numero usuario: ",numerousuario)
    #print("Depuracion variable numero secreto: ",numerosecreto)
    #print("Depuracion Distancia entre numeros: ",distanciaentrenumeros)
    if numerousuario>100 or numerousuario<0:
        print("Dije entre 0 y 100, no?")
        cantidadvidas=cantidadvidas-1     
    match numerousuario:
        case _ if (distanciaentrenumeros >=1 and distanciaentrenumeros <5):
            print("Casi la pegas ehhh,pero la erraste mal")
            cantidadvidas=cantidadvidas-1
        case _ if (distanciaentrenumeros >=5 and distanciaentrenumeros <10):
            print("Que calor que hace hoy no?")
            cantidadvidas=cantidadvidas-1
        case _ if (distanciaentrenumeros >=10 and distanciaentrenumeros <20):
            print("No esta nada mal pero tenes que mejorar")
            cantidadvidas=cantidadvidas-1
        case _ if (distanciaentrenumeros >=30 and distanciaentrenumeros <50):
            print("Estas lejos,Queres intentarlo de nuevo?")
            cantidadvidas=cantidadvidas-1
        case _ if (distanciaentrenumeros >=50 and distanciaentrenumeros <80):
            print("Yo que vos me dedico a otra cosa")
            cantidadvidas=cantidadvidas-1
        case _ if (distanciaentrenumeros >=80 and distanciaentrenumeros <=99):
            print("Estas tan lejos del numero como de conquistarla a ella, Sabelo")
            cantidadvidas=cantidadvidas-1
    if numerousuario==numerosecreto:
        print("Bien, ese era el numero,ahora podes realizar apuestas en la loteria")
        findeljuego="SI"
    if cantidadvidas==0:
        print("Perdiste, Mejor no te dediques a las apuestas")
        findeljuego="SI"


# Buen trabajo! Bien la idea de las vidas y las frases!



