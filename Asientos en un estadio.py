#Autor;Diana Marisol Medina Bravo
#Cálcula el total a pagar si se tienen 3 tipos de asientos

#Función para calcular el pago total de los asientos
#Recibe el número de asientos en A, el número de asientos en B y el número de asientos en c
#Y regresa el total de pago
def calcularPago(asientosA,asientosB,asientosC):
    totalPago=(asientosA*925)+(asientosB*775)+(asientosC*360)
    return totalPago

#Función principal, resuelve el problema
def main():
    asientosA= int(input("Número de boletos de clase A: "))
    asientosB = int(input("Número de boletos de clase B: "))
    asientosC = int(input("Número de boletos de clase C: "))
    totalPago=calcularPago(asientosA,asientosB,asientosC)
    print("El costo total es: $%.2f" % totalPago)

#Llama a la función main
main()




