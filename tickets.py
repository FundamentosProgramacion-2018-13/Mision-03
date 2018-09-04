# Autor:Jesús Emmanuel Alcalá Nava
# Descripción: calcular el total del precio de varios boletos
def calcularPago(boletos1, boletos2, boletos3):
    precio1 = boletos1 * 925
    precio2 = boletos2 * 775
    precio3 = boletos3 * 360
    total = precio1 + precio2 + precio3 #suma de lops precios de los boletos
    return total
def main():
    boletos1 = int(input("Número de boletos de clase A: "))
    boletos2 = int(input("Número de boletos de clase B: "))
    boletos3 = int(input("Número de boletos de clase C: "))
    total = calcularPago(boletos1, boletos2, boletos3)
    print("El costo total es: $%.2f" % total) #imprimir resultado
main()