# Autor: Silvia Ferman Muñoz
# Programa que pregunta cuantos boletos de cada tipo de asiento queire comprar e imprime el total a pagar.
# Demo Top-Down

# se calcula el pago total de los boletos usando el precio de cada uno
def calcularPago(asientosA, asientosB, asientosC):
    totalPago = (asientosA * 925) + (asientosB * 775) + (asientosC * 360)
    return totalPago

# Funcion principal donde se pregunta cuantos boletos compro por asiento y se imprimir el resultado
def main():
    numeroBoletosA = int(input("Número de asientos de clase A:"))
    numeroBoletosB = int(input("Número de asientos de clase B:"))
    numeroBoletosC = int(input("Número de asientos de clase C:"))
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El costo total es: $%.2f" % totalPago)


# Llama a la funcion principal
main()
