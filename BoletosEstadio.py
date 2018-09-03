# Autor: Jonathan Sanabria Rocha
# Calcular el costo total de los boletos del estadio


def calcularPago(asientosA,asientosB,asientosC):
#Multiplica el numero de boletos de cada clase por el precio de cada uno.

    totalpago = asientosA*925 + asientosB*775 + asientosC*360
    return totalpago




def main():
    asientosA = int(input("Numero de boletos clase A: "))
    asientosB = int(input("Numero de boletos clase B: "))
    asientosC = int(input("Numero de boletos clase C: "))
    totalpago = calcularPago(asientosA,asientosB,asientosC)


    print("El costo total es: $%.2f" % totalpago)

main()
