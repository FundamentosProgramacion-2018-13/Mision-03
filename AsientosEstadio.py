#Irma Gómez Carmona, A01747743
#Calcular el total a pagar dependiendo del tipo y número de boletos comprados

def calcularPago (asientosA , asientosB, asientosC):
    totalPago= asientosA*925+asientosB*775+asientosC*360
    return totalPago

def main ():
    numeroBoletosA= int(input("Numero de boletos de Clase A: "))
    numeroBoletosB = int(input("Numero de boletos de Clase B: "))
    numeroBoletosC = int(input("Numero de boletos de Clase C: "))
    totalPago= calcularPago(numeroBoletosA,numeroBoletosB,numeroBoletosC)

    print("El costo total es: $%.2f"%(totalPago))

main ()
