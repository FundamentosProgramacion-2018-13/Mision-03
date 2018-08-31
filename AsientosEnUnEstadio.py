# Autor: Erick David Ramírez Martínez, A01748155, Grupo: 2
# Descripción: Programa para calcular el costo de boletos en un estadio de acuerdo a la categoría y número de boletos que compre el cliente


def calcularPago(asientosA,asientosB,asientosC):
    costoDeBoletosA = asientosA*925
    costoDeBoletosB = asientosB*775
    costoDeBoletosC = asientosC*360

    totalPago = costoDeBoletosA + costoDeBoletosB + costoDeBoletosC

    return totalPago


def main():
    asientosA = int(input("Ingrese los boletos de clase A que desee comprar: "))
    asientosB = int(input("Ingrese los boletos de clase A que desee comprar: "))
    asientosC = int(input("Ingrese los boletos de clase A que desee comprar: "))

    pagoTotal = calcularPago(asientosA,asientosB,asientosC)

    print("El pago total por los boletos es de: $%0.2f" % (pagoTotal))


main()
