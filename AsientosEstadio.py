# Author: Ivan Honc Ayón     A01376466       Grupo 2
# Descripción: Este programa calcula el total a pagar por boletos para el estadio de fútbol.


def calcularPago(asientosA, asientosB, asientosC):
    precioA = asientosA*925
    precioB = asientosB*775
    precioC = asientosC*360
    totalPago = (precioA + precioB + precioC)

    return totalPago


def main():
    numBoletosA = float(input("Número de boletos de clase A: "))
    numBoletosB = float(input("Número de boletos de clase B: "))
    numBoletosC = float(input("Número de boletos de clase C: "))
    pagoTotal = calcularPago(numBoletosA, numBoletosB, numBoletosC)

    print("El costo total es: $%.2f" % pagoTotal)


main()
