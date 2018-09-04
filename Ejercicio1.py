#Autor: Alan Diaz Carrera
#Descripcion: Calcular el total a pagar por llos asientos en un estadio de futbol

def calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC):
    asientosA = numeroBoletosA *925
    asientosB = numeroBoletosB *775
    asientosC = numeroBoletosC *360
    totalPago = asientosA + asientosB + asientosC
    return totalPago

def main():
    numeroBoletosA = int(input("Numero de boletos de clase A:"))
    numeroBoletosB = int(input("Numero de boletos de clase B:"))
    numeroBoletosC = int(input("Numero de boletos de clase C:"))

    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El costo total es:", "$%.2f" % (totalPago))


main()