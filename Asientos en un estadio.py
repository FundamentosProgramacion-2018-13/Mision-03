# Autor: Oscar Alejandro Torres Maya, A01377686, grupo 04
# Descripción: Programa que calcula el área y perímetro del trapecio isóceles

# Función para calcular el pago total que hará el usuario dependiendo la categoría que éste elija
def calcularPago (asientosA, asientosB, asientosC) :
    totalPago = (asientosA*925)+(asientosB*775)+(asientosC*360)
    return totalPago

# Función principal, lee datos e imprime datos
def main() :
    asientosA = int(input("Número de boletos de clase A: "))
    asientosB = int(input("Número de boletos de clase B: "))
    asientosC = int(input("Número de boletos de clase C: "))
    total = calcularPago (asientosA, asientosB, asientosC)
    print("El costo total es: $%0.2f" % (total))

main()