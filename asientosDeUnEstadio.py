#Autor Claudio Mayoral García
#Descripción Se preguntará al usuario el numero de boletos de cada tipo y se desplegará el precio total


def calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC):
    # Calcula y guarda en la variable totalPago el total a pagar
    # Regresa pagoTotal
    pagoTotal = numeroBoletosA * 925 + numeroBoletosB * 775 + numeroBoletosC * 360
    return pagoTotal


def main():
    # numeroBoletosA = Leer el número de asientos de clase A
    # numeroBoletosB = Leer el número de asientos de clase B
    # numeroBoletosC = Leer el número de asientos de clase C
    # Calcula el resultado con la función calcularPago, envía como argumentos los valores leídos. Guarda el resultado.
    # Imprimir el resultado
    numeroBoletosA = int(input("Número de boletos de clase A: "))
    numeroBoletosB = int(input("Número de boletos de clase B: "))
    numeroBoletosC = int(input("Número de boletos de clase C: "))
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El costo total es: $%.2f" % totalPago)


# llama a la funcion "main"
main()
