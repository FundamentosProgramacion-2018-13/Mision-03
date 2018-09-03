# Autor: Juan Carlos Flores García, A01376511

# Descripción: Programa que calcule el total a pagar por los asientos de un estadio de fútbol.


# La siguiente función sirve para calcular el pago total.
def calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC):
    pagoTotal = (numeroBoletosA * 925) + (numeroBoletosB * 775) + (numeroBoletosC * 360)
    return pagoTotal


# La siguiente función sirve para imprimir el pago total.
def imprimir(totalPago):
    print("El total a pagar es: $%.2f" % totalPago)


# La siguiente función lee el número de los boletos A, B y C.
# También calcula el pago total con la función calcularPago e imprime el resultado con la función imprimir.
def main():
    numeroBoletosA = int(input("Número de boletos de clase A: "))
    numeroBoletosB = int(input("Número de boletos de clase B: "))
    numeroBoletosC = int(input("Número de boletos de clase C: "))
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    imprimir(totalPago)


 # Llama a la función main
main()

