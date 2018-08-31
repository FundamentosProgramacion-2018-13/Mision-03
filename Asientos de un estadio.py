# Autor: Zabdiel Valentin Garduño Vivanco, A01377950
# Descripcion: Calcular costo total de numero de asientos.



def calcularPago(asientosA, asientosB, asientosC):
    totalPago= asientosA*925+ asientosB*775+asientosC*360
    return totalPago


def main():
    numeroBoletosA=int(input("Numero de boletos clase A: "))
    numeroBoletosB=int(input("Numero de boletos clase B: "))
    numeroBoletosC=int(input("Numero de boletos clase C: "))
    costoTotal= calcularPago(numeroBoletosA,numeroBoletosB,numeroBoletosC)

    print("El costo total es: %.2f" %(costoTotal))


main()

