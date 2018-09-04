#Joshua Sánchez Martínez A01274269
#Pide al usuario la cantidad de boletos que desea para darle un costo el costo


def calcularPago(asientosA, asientosB, asientosC):

    totalPago = (asientosA*925)+(asientosB*775)+(asientosC*360)

    return totalPago


def main():

    numeroBoletosA = int(input("Asientos clase A: "))
    numeroBoletosB = int(input("Asientos clase B: "))
    numeroBoletosC = int(input("Asientos clase C: "))

    totalPago = calcularPago(numeroBoletosA,numeroBoletosB,numeroBoletosC)


    print("El costo total es: $ %.2f" % totalPago)

main()