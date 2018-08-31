# Autor: Alejandro Torices Oliva
# Programa que pregunta el número de asientos que quiere comprar e imprime el total a pagar.

#Calcula el costo total de todos los asientos comprados.
def calcularPago(asientosA, asientosB, asientosC):
    totalPago = (asientosA * 925) + (asientosB * 775) + (asientosC * 360)
    return totalPago

#Es la función principal, obtiene los datos e imprime las soluciones.
def main():
    numeroBoletosA = int(input("Número de boletos de clase A: "))
    numeroBoletosB = int(input("Número de boletos de clase B: "))
    numeroBoletosC = int(input("Número de boletos de clase C: "))
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El costo total es: $%.2f" % totalPago)


main()