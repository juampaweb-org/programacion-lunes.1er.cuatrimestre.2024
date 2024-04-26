"""# Gestor de Inventario de Tienda:Crea un sistema simple de gestión de inventario
para una tienda.El programa debe permitir agregar productos nuevos, 
actualizar la cantidad disponible de un producto y mostrar la lista actualizada 
de productos en stock."""


 
def Menu():
    print("Bienvenido al Gestor-Tienda\n")
    print("Eliga la opcion el cual corresponda tipeando 1 , 2 o 3 ")
    print("Si quiere ingresar un nuevo producto (1)")
    print("Si quiere actualizar un producto (2)")
    print("Si quiere salir del programa (3)")

def OpcionMenu(op):
    if op < 3 and op > 0:
        estado = True
    else:
        estado = False
    return estado

def BuscoProducto(listaProductos,buscar):
    estado = False
    for indice in range(len(listaProductos)):
        if listaProductos[indice] == buscar:
            indiceBuscado = indice
            estado = True
    if estado == False:
        indiceBuscado = 0
    return indiceBuscado

listaProductos = []

Menu()
opcion = int(input("Ingrese la opción: "))
while OpcionMenu(opcion):
    if opcion == 1:
        producto = input("Ingrese el nuevo producto: ")
        listaProductos.append(producto)
    elif opcion == 2:
        buscarProducto = input("Que producto quiere actualizar?: ")
        nuevoIndice = BuscoProducto(listaProductos,buscarProducto)
        if nuevoIndice != 0:
            nuevoProducto = input("Ingrese el nuevo producto: ")
            listaProductos.pop(nuevoIndice)
            listaProductos.insert(nuevoIndice,nuevoProducto)
        else:
            print("No se encontre el producto intente nuevamente.")
            buscarProducto = input("Que producto quiere actualizar?: ")
    Menu()
    opcion = int(input("Ingrese la opción: "))
        
print(listaProductos)


# Faltan cosas para ver el inventario, pero está muy bien, vamos a verlo más adelante cuando veamos diccionarios.
# falta cosas como la cantidad de los productos

