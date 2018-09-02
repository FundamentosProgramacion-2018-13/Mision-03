# Autor: Oscar Macias Rodríguez
# Descripción: Pregunta al usuario cuantos boletos quiere comprar para cada tipo de asiento e imprime el total a pagar.

# Calcula el costo de los asientos A, B y C. Además, calcula la suma de los asientos indicados (A, B y C)
def calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC):
    asientosA = numeroBoletosA * 925
    asientosB = numeroBoletosB * 775
    asientosC = numeroBoletosC * 360
    totalPago = asientosA + asientosB + asientosC
    return totalPago

# Imprime en pantalla el costo total de los boletos.
def main():
    numeroBoletosA = int(input("Numero de boletos de clase A:"))
    numeroBoletosB = int(input("Numero de boletos de clase B:"))
    numeroBoletosC = int(input("Numero de boletos de clase C:"))

    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)

    print("El costo total es:", "$%.2f" % totalPago)


main()