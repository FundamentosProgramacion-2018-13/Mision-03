#Autor: Marco González Elizalde A0137627
'''Propósito: Calcular el total a pagar dependiendo del tipo y cantidad de boletos
que se pidan e imprime el resultado'''

#Calcula el total a pagar dependiento del numero y tipo de boletos
def calcularPago(asientosA,asientosB,asientosC):
    costoA = asientosA * 925
    costoB = asientosB * 775
    costoC = asientosC * 360
    totalPago = costoA + costoB + costoC
    return totalPago

#Pide la cantidad de boletos de cada tipo que se va a pedir e imprime el total a pagar
def main():
    asientosA = float(input("Número de boletos de clase A: "))
    asientosB = float(input("Número de boletos de clase B: "))
    asientosC = float(input("Número de boletos de clase C: "))
    print("El costo total es: $%.02f" %(calcularPago(asientosA,asientosB,asientosC)))

#Corre el programa
main()
