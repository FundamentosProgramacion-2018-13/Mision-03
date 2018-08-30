#Jocelyn López Ortíz A01377451
#Cálculo del pago para comprar asientos en un estadio

def calcularPago(asientosA, asientosB, asientosC):
    totalPago = asientosA*925 + asientosB*775 + asientosC*360
    return totalPago

def main():
    numeroBoletosA = int(input("Número de boletos de classe A: "))
    numeroBoletosB = int(input("Número de boletos de classe B: "))
    numeroBoletosC = int(input("Número de boletos de classe C: "))
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print ("El costo total es: $%.2f" %(totalPago))

main()
