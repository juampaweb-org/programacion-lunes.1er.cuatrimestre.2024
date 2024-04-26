


"""
Vamos a realizar un programa que nos va a decir la nota promedio de un alumno en todo el cuatrimestre.
Dentro del cuatrimestre son 4 examenes y luego un examen final.
La aprobación del cuatrimestre es con nota 6 o mayor de promedio.
Y si el alumno tiene aprobada la cursada (es decir, obtuvo seis o más de 6 de promedio en sus 4 examenes, rinde el examen final)
Si el alumno tiene aprobada la cursada y el examen final, entonces el alumno aprobó la materia.

Entonces el programa debe preguntar por la nota de cada examen.
En función de las respuestas, primero debe avisar el promedio de las 4 notas de los examenes.
En caso de que el promedio sea mayor o igual a 6, debe avisar que el alumno tiene aprobada la cursada.
En caso de que el promedio sea menor a 6, debe avisar que el alumno no tiene aprobada la cursada.
Luego preguntar por nota del final (en caso de que haya aprobado la cursada), si es mayor o igual a 6, debe avisar que el alumno aprobó la materia.
En caso de que sea menor a 6, debe avisar que el alumno no aprobó el final de la materia, y puede rendir recuperatorio.



"""


notas_examenes = [float(input("Ingrese la nota del examen " + str(i+1) + ": ")) for i in range(4)]

suma_examenes = sum(notas_examenes)

promedio_examenes = suma_examenes / 4
print("Promedio de los cuatro examenes:", promedio_examenes)

if promedio_examenes >= 6:
    print("Aprobo la cursada.")
    
    nota_final = float(input("Nota examen final: "))
    
    if nota_final >= 6:
        print("Aprobo la materia.")
    else:
        print("No aprobo el final.")
else:
    print("No aprobo la cursada.")




# muy buen trabajo!

# la siguiente linea hacerla de manera mas simple para entenderla bien:
# notas_examenes = [float(input("Ingrese la nota del examen " + str(i+1) + ": ")) for i in range(4)]

