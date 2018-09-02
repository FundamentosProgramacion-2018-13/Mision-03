# Alex Fernando Leyva Martinez / A01747078
# Calcular el pago total de asientos

#Calcula el pago total en función del número de los boletos y su precio
def calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC):
    asientosa = int(numeroBoletosA * 925)
    asientosb = int(numeroBoletosB * 775)
    asientosc = int(numeroBoletosC * 360)
    totalPago = asientosa + asientosb + asientosc
    return totalPago

#Pregunta los datos y llama a las funciones anteriores
def main():
    numeroBoletosA = int(input("Número de boletos de clase A: "))
    numeroBoletosB = int(input("Número de boletos de clase B: "))
    numeroBoletosC = int(input("Número de boletos de clase C: "))
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("Número de boletos de clase A: ", numeroBoletosA)
    print("Número de boletos de clase B: ", numeroBoletosB)
    print("Número de boletos de clase C: ", numeroBoletosC)
    print("El costo total es: $%.2f" % (totalPago))


main()

