# Autor: Zoe Caballero Dominguez Matrícula: A01747247
# Descripción: Este programa calcula el costo de los asientos.

# Programa

# Función calcularPago recibe el número de boletos de cada clase y calcula el total a pagar, regresando éste resultado a la función main
def calcularPago (numeroBoletosA, numeroBoletosB, numeroBoletosC):
    asientosA = numeroBoletosA * 925
    asientosB = numeroBoletosB * 775
    asientosC = numeroBoletosC * 360
    costoTotal = asientosA + asientosB + asientosC
    return costoTotal


# Función main, lee el numero de boletos de cada clase, llama a la función de totalPago e imprime el costo total de los boletos.
def main():
    numeroBoletosA = int(input("Número de boletos de clase A: "))
    numeroBoletosB = int(input("Número de boletos de clase B: "))
    numeroBoletosC = int(input("Número de boletos de clase C: "))
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print ("El costo total es: $%.2f" % (totalPago))

# Llamar a la función main
main()
