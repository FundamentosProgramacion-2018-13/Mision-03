#Rodolfo Anibal Altamirano Sánchez, A01377949
#Se te proporciona la cantidad de boletos que se compraran de cada tipo para un concierto y se debe sacar el total
def calcularPago(boletoA, boletoB, boletoC):
    total= (boletoA*925)+(boletoB*775)+(boletoC*360)
    return total


def main():
    #Se te pide la cantidad de cada boleto
    boletoA = int(input("Número de boleteos de clase A: "))
    boletoB = int(input("Número de boleteos de clase B: "))
    boletoC = int(input("Número de boleteos de clase C: "))

    calcularPago(boletoA, boletoB, boletoC)
    total = calcularPago(boletoA,boletoB,boletoC)

    #Se imprime el costo total
    print("El costo total es de: $%.2f" % total)



main()