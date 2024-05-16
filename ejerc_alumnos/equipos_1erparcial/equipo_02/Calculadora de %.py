

# Calculadora de Propina:
# Desarrolla una calculadora de propinas que solicite al usuario ingresar el total de la cuenta en un restaurante. El programa debe calcular automáticamente diferentes opciones de propinas (por ejemplo, 15%, 18%, 20%) y mostrar el monto total a pagar incluyendo la propina.




Cuenta_Total = input("Total de la cuenta"" " "$")

if Cuenta_Total:
    Cuenta_Total = float(Cuenta_Total)
    
    Propina15 = Cuenta_Total * 0.15
    Total15 = Cuenta_Total + Propina15

    Propina18 = Cuenta_Total * 0.18
    Total18 = Cuenta_Total + Propina18

    Propina20 = Cuenta_Total * 0.20
    Total20 = Cuenta_Total + Propina20

    print("Opciones de propina:")
    print("15% de propina: $" + str(Propina15) + " - Total a pagar: $" + str(Total15))
    print("18% de propina: $" + str(Propina18) + " - Total a pagar: $" + str(Total18))
    print("20% de propina: $" + str(Propina20) + " - Total a pagar: $" + str(Total20))

opcion = input("Seleccione una opcion de propina (1, 2 o 3): ")

if opcion == "1":
        print("Seleccionaste 15%.")
        print("Total a pagar: $" + str(Total15))
if opcion == "2":
        print("Seleccionaste 18%.")
        print("Total a pagar: $" + str(Total18))
if opcion == "3":
        print("Seleccionaste 20%.")
        print("Total a pagar: $" + str(Total20))



# como estandarizacion siempre tratemos de usar minusculas en las variables. Y guiones bajos para separar.

# revisar por que esta mal calculado.

# pongo lo que me dió

# Total de la cuenta $12000
# Opciones de propina:
# 15% de propina: $1800.0 - Total a pagar: $13800.0
# 18% de propina: $2160.0 - Total a pagar: $14160.0
# 20% de propina: $2400.0 - Total a pagar: $14400.0
# Seleccione una opcion de propina (1, 2 o 3): 2
# Seleccionaste 18%.
# Total a pagar: $14160.0

