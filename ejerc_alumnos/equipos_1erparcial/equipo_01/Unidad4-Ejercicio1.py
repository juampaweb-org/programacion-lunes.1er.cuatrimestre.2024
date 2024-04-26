# Unidad 4 - Ejercici20o 1


#Crear una variable con valor 20 va a ser como referencia el minimo.
minimo= 20

#Otra con valor de 500, va a ser como referencia el maximo.
maximo= 500

#Luego pregunta al usuario por un valor, almacenarlo en otra variable, forzar a que ponga un numero, sino preguntar repetidamente.
valor= input("ingresar un valor: ")

#Ese numero transformarlo en integer
valor= int(valor)

#Ahora imprimir en pantalla.
print(valor)

#Si el numero que puso el usuario es menor que el valor minimo definido mostrar el texto VALOR BAJO
if valor < minimo:
    print ("VALOR BAJO")

#Si el numero que puso el usuario es mayor que el valor maximo definido mostrar el texto VALOR ALTO
elif valor > maximo:
    print("VALOR ALTO")

#Si el numero que puso el usuario esta entre el valor minimo y el valor maximo mostrar el texto VALOR MEDIO
else:
    print("VALOR MEDIO")







# Buen trabajo!  faltó agregar el método .isdigit() que les había dicho en clase, por si el usuario ingresa un valor que no es un número.




