# Calculadora de Propina:
# Desarrolla una calculadora de propinas que solicite al usuario ingresar el total de la cuenta 
#en un restaurante.
# El programa debe calcular automáticamente diferentes opciones de propinas 
#(por ejemplo, 15%, 18%, 20%) y mostrar el monto total a pagar incluyendo la propina.


#COMIENZA EL CODIGO
totalpagar=input("Ingrese Monto a Pagar:"+" ")
if int(totalpagar)>0:
  Propina1=int(totalpagar)+(int(totalpagar)*15)/100
  Propina2=int(totalpagar)+(int(totalpagar)*18)/100
  Propina3=int(totalpagar)+(int(totalpagar)*20)/100
else:
  totalpagar=input("Ingrese Monto a Pagar:"+" ")
print("La propina con un 15% mas:"+" "+str(Propina1))
print("La propina con un 18% mas:"+" "+str(Propina2))
print("La propina con un 20% mas:"+" "+str(Propina3))
print("Fin del programa")


# realizar un input e if() para que me pregunte que porcentaje y mostrar solamente ese porcentaje...