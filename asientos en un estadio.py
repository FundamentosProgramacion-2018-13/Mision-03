# Autor: Rubén Villalpando Bremont
# El programa te imprime el total a pagar con la compra de algunos boletos de diferentes costos

# Esta función calcula el pago total a partit del número de boletos ingresados
def calcularPago (asientosA, asientosB, asientosC):
    totalPago = asientosA*925 + asientosB*775 + asientosC*360
    return totalPago

# función main que pide el número de boletos al usuario e imprime el total a pagar
def main():
    numeroBoletosA = int(input("Número de boletos de clase A: "))
    numeroBoletosB = int(input("Número de boletos de clase B: "))
    numeroBoletosC = int(input("Número de boletos de clase C: "))
    totalPago = calcularPago (numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El costo total es: $%.2f" % (totalPago))

# Llamar a main
main()





