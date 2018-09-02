# Luis Jonathan Rosas Ramos
# calculando un total a pagar basandose en un numero de asientos


def calcularPago(asientosA,asientosB,asientosC):
    # entendemos que los parametros que se van a utilizar son en relacion a numero de asientos en cada zona
    numeroBoletosA = asientosA
    numeroBoletosB = asientosB
    numeroBoletosC = asientosC
    # total va a ser igual a la suma de el numero de asientos de cada zona, por el precio del lugar
    totalPago = (asientosA*925)+(asientosB*775)+(asientosC*360)
    return totalPago


def main():
    # Preguntar los asientos en A,B,C
    numeroBoletosA = int(input("Tecle los asientos en A: "))
    numeroBoletosB = int(input("Tecle los asientos en B: "))
    numeroBoletosC = int(input('Tecle los asientos en C: '))
    # Calcular el total con los parametros de A,B,C
    total = calcularPago(numeroBoletosA,numeroBoletosB,numeroBoletosC)
    # finalmente imprimimos el total
    print("tu total es de: $ %.2f " % total)

#Llamar a la funcion principal
main()