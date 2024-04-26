print("1. Calcular el area y el perimetro de un circulo.")
print("2. Calcular el area y el perimetro de un cuadrado.")
print("3. Calcular el area de un triangulo.")
print("4. Salir del programa.")

#Seleccionamos una opcion

opcion = input("Selecciona una opcion: ")

if opcion == "1":
        radio = float(input("Ingresa el radio del circulo: "))
        area_circulo = radio ** 2
        perimetro_circulo = 2 * radio
        print("area del circulo:", area_circulo)
        print("Perimetro del circulo:", perimetro_circulo)
if opcion == "2":
        lado = float(input("Ingresa el lado del cuadrado: "))
        area_cuadrado = lado ** 2
        perimetro_cuadrado = 4 * lado
        print("area del cuadrado:", area_cuadrado)
        print("Perimetro del cuadrado:", perimetro_cuadrado)
if opcion == "3":
        base = float(input("Ingresa la base del triangulo: "))
        altura = float(input("Ingresa la altura del triangulo: "))
        area_triangulo = 0.5 * base * altura
        print("area del triangulo:", area_triangulo)
if opcion == "4":
        print("Fin del programa")
    



# están algunas formulas mal.. revisar y rehacer. Utilizar PI del modulo math para resolver el circulo por ejemplo..