"""
Pedirle al usuario que escriba una frase completa.
Luego imprimir en pantalla cantidad de veces que aparece cada vocal en la frase.
Ejemplo:
a -> 5
e -> 3
i -> 2
o -> 0
u -> 1

Preguntar si quiere hacerlo nuevamente y volver a comenzar o terminar la ejecución.
"""
continuar = 's'


def numero_vocales(frase):
    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0
    for caracter in frase:
        if caracter == 'a':
            contador_a += 1
        elif caracter == 'e':
            contador_e += 1
        elif caracter == 'i':
            contador_i += 1
        elif caracter == 'o':
            contador_o += 1
        elif caracter == 'u':
            contador_u += 1
    print("a->" + str(contador_a) + "\ne->" + str(contador_e) + "\ni->" + str(contador_i) + "\no->" + str(
        contador_o) + "\nu->" + str(contador_u))


while continuar == 's' or continuar == 'S':
    print("Escriba una frase completa: ")
    frase_completa = input()
    numero_vocales(frase_completa)
    print("Desea continuar operando? s/n: ")
    continuar = input()
