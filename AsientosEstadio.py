#Autor: Luisa Fernada Arellano Alvarado A01377974





def calcularPago(numeroBoletosA,numeroBoletosB, numeroBoletosC):
    Pago = numeroAsientosA * 925
    Pago = Pago + numeroBoletosB * 775 + numeroBoletosC * 360
    return Pago



  


def main():
    numeroBoletosA = int(input("Teclea número de boletos de clase A:"))
    numeroBoletosB = int(input("Teclea número de boletos de clase B:"))
    numeroBoletosC = int(input("Teclea número de boletos de clase C:"))
    total = calcularPago
 
    


# Llamamos a la función main

main()
