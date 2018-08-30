# Autor: Luis Humberto Burgueño Paz
# El programa pregunta al usuario la cantidad y el tipo de boletos que quiere comprar e imprime el total a pagar

# Recibe como parámetros el número de asientos de cada clase que el usuario desea comprar y regresa el total a pagar
def calcularPago(asientosA, asientosB, asientosC):
   totalPago = (asientosA*925) + (asientosB*775) + (asientosC*360)
   return totalPago

# Pide al usuario la cantidad de boletos de cada clase de asiento y los envía a la función calcularPago, posteriormente imprime el resultado
def main():
   numeroBoletosA = int(input("Número de boletos de clase A: "))
   numeroBoletosB = int(input("Número de boletos de clase B: "))
   numeroBoletosC = int(input("Número de boletos de clase C: "))
   totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
   print("El costo total es: $%.02f" % totalPago)


main()
