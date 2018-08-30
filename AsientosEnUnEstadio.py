# Emiliano Heredia Garcia A01377072
# Calcula el costo total en base a la cantidad de asientos en las diferentes clases (A, B, C)

def calcularPago(asientosA, asientosB, asientosC) :

    #Calcula el pago total tomando como argumentos la cantidad de asientos de clase A, B y C.

    pagoT = (asientosA*925)+(asientosB*775)+(asientosC*360)

    return pagoT


def main():
    asientosA = int(input("Número de boletos de clase A: "))
    asientosB = int(input("Número de boletos de clase B: "))
    asientosC = int(input("Número de boletos de clase C: "))
    pagoTotal = calcularPago(asientosA, asientosB, asientosC)
    print("El costo total es: %.2f" %pagoTotal)

main()