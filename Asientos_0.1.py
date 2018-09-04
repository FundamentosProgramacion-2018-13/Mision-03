#Autor: Daniel Cordova Bermudez
#Descripción: En este programa calcula el precio total de los asientos clase A,B y C.

def calcularPago(asientosA, asientosB, asientosC) :
    totalPago = (asientosA*925)+(asientosB*775)+(asientosC*360)
    return totalPago

def main() :
    numeroBoletosA = int(input("Numero de boletos de asientes en clase A:"))
    numeroBoletosB = int(input("Numero de boletos de asientes en clase B:"))
    numeroBoletosC = int(input("Numero de boletos de asientes en clase C:"))
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El costo total es: $%.2f" % totalPago)

main()