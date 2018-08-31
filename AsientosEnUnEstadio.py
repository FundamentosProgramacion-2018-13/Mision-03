#Autor: Jesus Zabdiel Sanchez Chavez A01374964

#Descripcion: Calcula el costo total al elegir un numero de asientos de cada tipo.


#función principal
def main ():
    numeroBoletosA = int (input("Cantidad de asientos de tipo A " ))
    numeroBoletosB = int(input("Cantidad de asientos de tipo B "))
    numeroBoletosC = int(input("Cantidad de asientos de tipo C "))
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print ("El costo total es: $%.2f" % (totalPago))


#Calcula el pago por todos los asientos
def calcularPago (asientosa, asientosb, asientosc):
    totalPago = (asientosa * 925) + (asientosb *775) + (asientosc * 360)
    return totalPago

main ()