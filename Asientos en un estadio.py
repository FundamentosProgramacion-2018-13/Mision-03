# Carlos Badillo García             A01377618
# Programa que pregunta al usuario cuantos boletos quiere comprar para cada tipo de asiento y que imprima el total a pagar

def calcularPago(asientosA, asientosB, asientosC):  #Función que sirve para calcular el pago total de todos los boletos comprados dependiendo la clase
    costoAsientosA = asientosA*925
    costoAsientosB = asientosB*775
    costoAsientosC = asientosC*360
    totalPago = costoAsientosA + costoAsientosB + costoAsientosC
    return totalPago

def main(): #Función que sirve para que el usuario introduzca el numero de boletos de la clase A, B y C y además imprime el costo total
    asientosA = int(input("Número de boletos de clase A: "))
    asientosB = int(input("Número de boletos de clase B: "))
    asientosC = int(input("Número de boletos de clase C: "))
    totalPago = print("El costo total es: $%.2f" % calcularPago(asientosA, asientosB, asientosC))

main()