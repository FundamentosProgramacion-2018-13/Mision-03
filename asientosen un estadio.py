# JavierAlexandro Vargas Sánchez A01377718
'''Programa que calcula el precio total al comprar boletos con costo diferente,
suma el total de precios e imprime costo total'''


def calcularBoletosA(noBoletosA): # calcula el precio total de los boletos clase A
    precioTotalA = noBoletosA * 925
    return precioTotalA

def calcularBoletosB(noBoletosB): # calcula el precio total de los boletos clase B
    precioTotalB = noBoletosB * 775
    return precioTotalB

def calcularBoletosC(noBoletosC): # calcula el precio total de los boletos clase C
    precioTotalC = noBoletosC * 360
    return precioTotalC

def calcularPrecioTotal(precioTotalA, precioTotalB, precioTotalC): # Suma todos los precios para calcular el costo final
    precioTotal = precioTotalA + precioTotalB + precioTotalC
    return precioTotal

def imprimir(  precioTotal): #Imprime el costo total

    print("El costo total es: $",format(precioTotal,".2f" ))

def main():
    noBoletosA = int(input("Número de boletos de clase A: "))
    noBoletosB =int(input("Número de boletos de clase B: "))
    noBoletosC = int(input("Número de boletos de clase C: "))
    precioTotalA = calcularBoletosA(noBoletosA)
    precioTotalB = calcularBoletosB(noBoletosB)
    precioTotalC = calcularBoletosC(noBoletosC)
    precioTotal = calcularPrecioTotal(precioTotalA, precioTotalB, precioTotalC)
    imprimir ( precioTotal)

main()