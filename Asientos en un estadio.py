"""
Nombre: Alexys Martín Coate Reyes
Martícula: A01746998

Descripción: Calcular el costo total de los asientos dependientemente del tipo de asientos que sean.
"""

#Calcula el costo total de los asientos con base al tipo de asiento elegido y a su cantidad
def costoTotal(asientosA, asientosB, asientosC):
    total = (asientosA*925) + (asientosB*775) + (asientosC*360)
    return total

#Imprime el número de asientos pedidos y el costo total de los asientos
def imprimir(asientosA, asientosB, asientosC, total):
    print("Número de boletos de clase A: %d" % (asientosA))
    print("Número de boletos de clase B: %d" % (asientosB))
    print("Número de boletos de clase C: %d" % (asientosC))
    print("El costo total es: $%.2f" % (total))

#Función principal que engloba toda la serie de pasos para resolver el resultado. También obtiene los datos de entrada.
def main():
    asientosA = int(input("Número de boletos de clase A: "))
    asientosB = int(input("Número de boletos de clase B: "))
    asientosC = int(input("Número de boletos de clase C: "))
    total = costoTotal(asientosA, asientosB, asientosC)
    imprimir(asientosA, asientosB, asientosC, total)

#Llama a la función principal para que se ejecute
main()