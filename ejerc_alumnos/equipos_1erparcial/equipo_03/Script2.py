""" Lista de Tareas Pendientes:
Crea un programa que permita al usuario mantener una lista de tareas pendientes. 
El programa debe permitir agregar tareas nuevas, marcar tareas como completadas
y mostrar la lista actualizada de tareas."""

def MostrarIngreso():
    print("Para ingresar una tarea escriba 't'.\n")
    print("Para marcar una tarea completada escriba 'c'.\n")
    print("Para salir escriba 'f'.\n")


def TareaCompleta(tarea , tareasPendientes):
    for indice in range(len(tareasPendientes)):
        if tareasPendientes[indice] == tarea :
            print("Tarea: ", tareasPendientes[indice] , "se ha completado, y por ende se eliminara.")
            tareasPendientes.pop(indice)


def MostrarTareasPendientes(tareasPendientes):
    print("Quedaron las siguientes tareas pendientes:")
    print("\n")
    if len(tareasPendientes) == 0:
        print("No hay tareas pendientes.")
    else:
        for indice in range(len(tareasPendientes)):
          print("\n ", tareasPendientes[indice])
    
tareasPendientes = []

MostrarIngreso()
instruccion = input("Su elección: ")
indice = 0
while instruccion != 'f':
    if instruccion == 't':
        tarea = input("Ingrese el la tarea pendiente:")
        tareasPendientes.append(tarea)
    elif instruccion == 'c':
        tareaCompleta = input("Que tarea quiere marcar como completa: ")
        TareaCompleta(tareaCompleta , tareasPendientes)
    
    MostrarIngreso()
    instruccion = input("Su elección: ")



MostrarTareasPendientes(tareasPendientes)
    


# está muy bien, hay muchas cosas que las vamos a ver más adelante, no me dí cuenta en éstos ejercicios que les dí...




