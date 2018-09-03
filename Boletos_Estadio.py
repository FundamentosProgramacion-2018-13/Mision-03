#Autor: David Rodriguez
#Calcula costo total en base al tipo (A, B o C) y número de boletos solicitados
#Y entrega el número de boletos de cada tipo solicitados y el costo total


#Calcula el costo total en base al tipo de boletos y al número de boletos solicitados
def calcularPago(asientosA, asientosB, asientosC):
    costoA = asientosA*925
    costoB = asientosB*775
    costoC = asientosC*360
    totalPago = costoA + costoB + costoC
    return totalPago

def imprimir(totalPago):
    print("El costo total es: $%.2f" % (totalPago))

#Pide cantidad de cada tipo de boleto
#Imprime el número de boletos y el costo total
def main():
    asientosA = int(input("Número de boletos clase A:"))
    asientosB = int(input("Número de boletos clase B:"))
    asientosC = int(input("Número de boletos clase C:"))
    totalPago = calcularPago(asientosA, asientosB, asientosC)
    imprimir(totalPago)

#Llama a la función principal
main()

