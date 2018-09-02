# Mariana Caballero Cabrera A01376544

# A continuación voy a escribir un programa que prengunte al usuario el número de boletos que desea comprar
# y el programa va a calcular el total que debe pagar dependiendo del número de boletos que requiera




# esta función calcula el total de lo que se va a pagar por los boletos según los asientos

def calcularPago (asientosA, asientosB, asientosC):
    totalAsientosA = asientosA*925
    totalAsientosB = asientosB * 775
    totalAsientosC = asientosC * 360
    totalPago = totalAsientosA +totalAsientosB + totalAsientosC

    return totalPago


# esta función imprime el resultado total

def imprimir (totalPago):
    print ("El costo total es: $%5.2f" % (totalPago))



# esta es la función principal

def main ():
    asientosA = int (input ( "Número de boletos de clase A: "))
    asientosB = int (input ("Número de boletos de clase B: "))
    asientosC = int (input ("Número de boletos de clase C: "))

    totalPago = calcularPago (asientosA,asientosB, asientosC)
    imprimir (totalPago)


#llamamos a la función principal
main()