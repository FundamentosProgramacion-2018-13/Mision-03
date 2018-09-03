#Autor: Michelle Sánchez Guerrero
#Descripción: Programa que calcula el total a pagar de la cantidad de boletos deseados.

#Función que calcula el pago total de los diferentes boletos
def calcularPago(asientosA, asientosB, asientosC):
    asientosA = asientosA * 925
    asientosB = asientosB * 775
    asientosC = asientosC * 360
    totalPago = asientosA + asientosB + asientosC
    return totalPago

#Función principal. Lee datos e imprime resultados.
def main():
    numeroBoletosA = int(input("Número de boletos de clase A: "))
    numeroBoletosB = int(input("Número de boletos de clase B: "))
    numeroBoletosC = int(input("Número de boletos de clase c: "))
    total = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El costo total es: $%.02f" % (total))

#Llamar a la función principal
main()