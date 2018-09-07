#Autor: Luisa Fernada Arellano Alvarado A01377974


def calcularPago(AsientoA,AsientoB, AsientoC):
    totalPago = AsientoA*925 + AsientoB*775 + AsientoC*360
    return totalPago



def main():
    numeroBoletosA = int(input("Teclea número de boletos de clase A: "))
    numeroBoletosB = int(input("Teclea número de boletos de clase B: "))
    numeroBoletosC = int(input("Teclea número de boletos de clase C: "))
    totalPago = calcularPago(numeroBoletosA,numeroBoletosB,numeroBoletosC)
 
    print("El costo total es: $%.2d"%(totalPago))


# Llamamos a la función main

main()
