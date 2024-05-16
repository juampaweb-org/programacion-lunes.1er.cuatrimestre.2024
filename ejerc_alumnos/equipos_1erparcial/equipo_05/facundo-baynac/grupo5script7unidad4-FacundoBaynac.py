# Utilice como valor de pi el valor 3.141592
pi = 3.141592

# Calcula el área del círculo según el radio dado
def calcular_area_circulo(radio_circulo):
  area_circulo = radio_circulo * pi ** 2
  print("El área del círculo es: " + str(area_circulo))

# Calcula el área del triangulo según la base y la altura dada
def calcular_area_triangulo(base_triangulo, altura_triangulo):
  area_triangulo = base_triangulo * altura_triangulo / 2
  print("El área del triángulo es: " + str(area_triangulo))

# Pregunte primero si se quiere calcular el área de un triángulo o la de un círculo
print("Quiere calcular el área de un triángulo(T) o la de un círculo(C)\nIngrese la letra T o C : ")
triangulo_circulo = input()

if triangulo_circulo == "c" or triangulo_circulo == "C" :
  print("\nIngrese el radio del círculo que queire calcular: ")
  calcular_area_circulo(int(input()))

elif triangulo_circulo == "t" or triangulo_circulo == "T" :
  print("\nIngrese la base del triángulo que queire calcular: ")
  base_triangulo = int(input())
  print("\nIngrese la altura del triángulo que queire calcular: ")
  altura_triangulo = int(input())
  calcular_area_triangulo(base_triangulo, altura_triangulo)
  
else :
  print("\nUsted ingresó un valor incorrecto.\n")


  # utilizar pi desde el modulo math de Python
  # agregar figura que falta... cuadrado