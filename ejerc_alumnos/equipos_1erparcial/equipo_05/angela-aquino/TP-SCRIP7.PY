#Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. Si se contesta que se quiere calcular el área de un 
#triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de 
#un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.
#Se recuerda que el área de un triángulo es base por altura dividido por 2 y que el área de un círculo es Pi (aproximadamente 3,141592) por el radio al cuadrado.
#Nota: Utilice como valor de pi el valor 3.141592.


# comienza el codigo

dato=input("Quiere calcular el área de un triángulo(T o t) o la de un círculo(C o c)"+ " ")

if dato=="T" or dato=="t":
   base=input("Ingese la base del triangulo"+" ")
   altura=input("Ingrese la altura del triangulo"+" ")
   areaT=(int(base)*int(altura))/2
   print("El area de un triangulo es:  "+ str(areaT))
else:
  if dato=="C" or dato=="c":
      radio=input("Ingese el radio del circulo"+" ")  
      areaC=(int(radio)*float(3.141592))**2
      print("El area de un circulo es:  "+ str(areaC))
print("Fin del programa")


# # buen trabajo!
# Agregar la figura que falta
# y utilizar a pi desde el modulo math de Python