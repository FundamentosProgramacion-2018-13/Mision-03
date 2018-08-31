#Autor: Samantha MArtínez Franco A01747686
#Descripción: calcular cuanto va a pagar una persona por comprar boletos de un estadio en diferentes clases

def calcularPago(asientosA, asientosB, asientosC):  #función que calcula pago total de los asientos
    pagoA=asientosA*925
    pagoB=asientosB*775
    pagoC=asientosC*360
    pagototal=pagoA+pagoB+pagoC
    return pagototal



def main():    #función principal
    asientosA = int(input("Número de boletos de clase A: "))  #llamar valores
    asientosB = int(input("Número de boletos de clase B: "))
    asientosC = int(input("Número de boletos de clase C: "))
    pagototal=calcularPago(asientosA, asientosB, asientosC)  #valor de pago total
    print("El costo total es: $%.2f" % (pagototal))  #imprimir valores

#llamar función principal
main()
