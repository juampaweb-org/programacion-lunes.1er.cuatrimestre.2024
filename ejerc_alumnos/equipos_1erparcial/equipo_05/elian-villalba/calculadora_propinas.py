#Consigna: 
# Calculadora de Propina:
# Desarrolla una calculadora de propinas que solicite al usuario ingresar el total de la cuenta en un restaurante. El programa debe calcular automáticamente diferentes opciones de propinas (por ejemplo, 15%, 18%, 20%) y mostrar el monto total a pagar incluyendo la propina.

def calcular_propina(cuenta, porcentaje_propina):
    propina = cuenta * (porcentaje_propina / 100)
    total_a_pagar = cuenta + propina
    return propina, total_a_pagar

def main():
    total_cuenta = float(input("Ingrese el total de la cuenta en el restaurante: $"))

    porcentajes_propina = [15, 18, 20]

    print("Calculadora de Propina:")
    for porcentaje in porcentajes_propina:
        propina, total_a_pagar = calcular_propina(total_cuenta, porcentaje)
        print(f"Si la propina es de un {porcentaje}%, el total a pagar sería de: ${total_a_pagar:.2f} (la propina es de: ${propina:.2f})")

if __name__ == "__main__":
    main()




# buen trabajo!

# agregar que consulte que porcentaje quiere pagar de propina y entregar solamente ese resultado..