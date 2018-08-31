# David Isaí Llópez Jaimes  A01748363
# Calcula el total a pagar por los boletos que se quieren

# Calcula el precio total de los boletos de las clases juntas
def calcularPago (asientosA, asientosB, asientosC):
    totalPago = asientosA * 925
    totalPago = asientosB * 775 + totalPago
    totalPago = asientosC * 360 + totalPago
    return totalPago

def main():
    numeroBoletosA = int(input("Número de boletos de clase A: "))
    numeroBoletosB = int(input("Número de boletos de clase B: "))
    numeroBoletosC = int(input("Número de boletos de clase C: "))

    pagoTotal = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC )

    print("El costo total es: $",format(pagoTotal, ".2f"))

# Llama a la función principal (algoritmo)
main()

