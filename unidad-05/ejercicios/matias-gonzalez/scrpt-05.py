
# Gestor de Inventario de Tienda:
# Crea un sistema simple de gestión de inventario para una tienda. El programa debe permitir agregar productos nuevos, actualizar la cantidad disponible de un producto y mostrar la lista actualizada de productos en stock.




# Crear un diccionario para almacenar el inventario de la tienda
inventario = {}


# Función para agregar un producto nuevo al inventario
def agregar_producto():
    nombre = input("Ingresa el nombre del producto: ")
    cantidad = int(input("Ingresa la cantidad disponible del producto: "))
    inventario[nombre] = cantidad
    print(f"Producto '{nombre}' agregado al inventario.")

# Función para actualizar la cantidad disponible de un producto
def actualizar_producto():
    nombre = input("Ingresa el nombre del producto a actualizar: ")
    if nombre in inventario:
        nueva_cantidad = int(input("Ingresa la nueva cantidad disponible: "))
        inventario[nombre] = nueva_cantidad
        print(f"Cantidad del producto '{nombre}' actualizada.")
    else:
        print(f"El producto '{nombre}' no está en el inventario.")

# Función para mostrar la lista actualizada de productos en stock
def mostrar_inventario():
    print("Inventario actualizado:")
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad} unidades")

# Menú de opciones para el usuario
while True:
    print("\nBienvenido al Gestor de Inventario de Tienda")
    print("1. Agregar producto")
    print("2. Actualizar cantidad de producto")
    print("3. Mostrar inventario")
    print("4. Salir")

    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        actualizar_producto()
    elif opcion == "3":
        mostrar_inventario()
    elif opcion == "4":
        print("Gracias por usar el Gestor de Inventario. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida (1-4).")