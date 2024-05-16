
# Gestor de Inventario de Tienda:
# Crea un sistema simple de gestión de inventario para una tienda. El programa debe permitir agregar productos nuevos, actualizar la cantidad disponible de un producto y mostrar la lista actualizada de productos en stock.


lista = ["monitor", "pc", "monitor"]

#Incia el menu de opciones
comprobar = True      #agregamos la variable comprobar para que se genere el bucle          

while comprobar:        
    consultar = int(input("""Que deseas hacer

    (1) Consultar
    (2) Agregar nuevo producto
    (3) Mostrar stock
    (4) Ingresar cantidad 
    (5) Salir
    """))

    #Opcion consulta
    if consultar == 1:
        stock = input("consulta producto: ")
        print(lista.count(stock))   #Imprime cuantas veces se repite el producto ingresado
        print ("")

    #Opcion Agregar producto    
    elif consultar == 2:
        #agregar = input("Agregar producto: ")
        #nprod = 
        lista.append(input("Ingresa el nuervo producto: "))  #Se agrega el producto en caso no existe
        print ("Se agregó el producto") 
        print ("")

    #Opcion consultar stock
    elif consultar == 3:
        print(lista)        #Imprime todos los productos en stock
        print ("")

    #Opcion agregar productos
    elif consultar == 4:
        ingresa = input("ingresa producto")
        qty = int(input("cantidad"))

        for i in range(qty):            #Se crea la variable i que se repite las veces ingresadas 
            i=  lista.append(ingresa)   #Se 
            print("se ingresaron")
            print(lista)

    #Opcion salir
    else:
        break