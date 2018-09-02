# Autor: Alex Serrano Durán
# Este programa calcula el total a pagar al comprar distintos boletos


def calcularPago(boletosA, boletosB, boletosC):     # Se calcula el total según los boletos comprados
    precioA = boletosA * 925
    precioB = boletosB * 775
    precioC = boletosC * 360
    totalPago = precioA + precioB + precioC
    return totalPago


def main():             # Función main, pide la cantidad de boletos e imprime el costo
    boletosA = int(input("Número de boletos de clase A: "))
    boletosB = int(input("Número de boletos de clase B: "))
    boletosC = int(input("Número de boletos de clase C: "))
    totalPago = calcularPago(boletosA, boletosB, boletosC)
    print("El costo total es: $%.2f" % totalPago)


main()



