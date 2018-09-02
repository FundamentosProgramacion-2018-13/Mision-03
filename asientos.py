#Autor: Víctor Manuel Rodríguez Loyola.  A01747755
#Descripción: Este programa calcula el total a pagar al comprar boletos de diferentes categorías en un estadio.


def calcularPago(asientosA, asientosB, asientosC):  #Calcula el pago total de acuerdo al precio de cada asiento
    totalPago= asientosA*925 + asientosB*775 + asientosC*360
    return totalPago


def main():
    numeroBoletosA = int(input("Número de boletos clase A: "))
    numeroBoletosB = int(input("Número de boletos clase B: "))
    numeroBoletosC = int(input("Número de boletos clase C: "))
    totalPago= calcularPago(numeroBoletosA,numeroBoletosB,numeroBoletosC)
    print("El costo total es: $%.2f" % totalPago)


main()



