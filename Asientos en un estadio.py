#Nombre: Saúl Figueroa Conde.
#Matrícula: A01747306.
#Programa: Este programa indica al usuario el precio final de los boletos para un estadio de fútbol, dependiendo
#del tipo de asiento y la cantidad de boletos.

#Aquí se define la función calcularPago que recibe como parámetros el número de boletos por asiento de cada
#clase y regresa el total a pagar.

def calcularPago(asientosA, asientosB, asientosC):
    totalPago = asientosA * 925
    totalPago = (asientosB * 775) + totalPago
    totalPago = (asientosC * 360) + totalPago
    return totalPago

#Ésta es la función main. Se le pide al usuario la cantidad de boletos que quiere de cada asiento. Los valores
#indicados se envían a la función calcularPago para que regrese el costo total. Por último, se imprime el resultado
#con dos decimales de precisión.

def main():
    numeroBoletosA = float(input("Número de boletos de clase A:"))
    numeroBoletosB = float(input("Número de boletos de clase B:"))
    numeroBoletosC = float(input("Número de boletos de clase C:"))

    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El costo total es: $%.2f" % (totalPago))

#El programa llama aquí a la función main para resolver el problema en cuestión, calculando el costo total de los boletos.
main()