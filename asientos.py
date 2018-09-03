#encoding: UTF-8
#Autor: Alek Howland, A01747765
#Descripcion: Un programa que usa funciones para calcular el total de pago de 3 tipos de asientos diferentes solicitados
# por el usuario


def main(): #Función principal
    A = int(input("Número de boletos de clase A: "))
    B = int(input("Número de boletos de clase B: "))
    C = int(input("Número de boletos de clase C: "))
    calcularPago(A, B, C)
    imprimir(calcularPago(A, B, C))


def calcularPago(A, B, C): #Calcula el pago dependiendo el precio de cada tipo de asiento
    claseA = A * 925
    claseB = B * 775
    claseC = C * 360 
    totalPago = claseA + claseB + claseC
    return totalPago

def imprimir(totalPago): #Imprime los resultados
    print ("El costo total es: $ %.2f" % (totalPago))


main() #Se llama a la función principal



