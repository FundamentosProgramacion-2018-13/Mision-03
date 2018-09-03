# Damián Iván García Ravelo
# A01376354
#Programa que calcula el precio a pagar por número de asientos

#Declarar la función para calcular el precio de A,B y C; finalmente sumarlos
def calcularCosto (boletosA, boletosB, boletosC) : #La función de calcular costo va a ser dada por el precio
    #de cada boleto y multiplicado por el número de boletos pedidos
    totalA = boletosA * 925 #El total de A= cantidad de boletos pedidos por el precio base
    totalB = boletosB * 775 #El total de B= cantidad de boletos pedidos por el precio base
    totalC = boletosC * 360 #El total de C= cantidad de boletos pedidos por el precio base
    precio = totalA + totalB + totalC
    return precio #pide el regreso de precio que es la suma de los totales


def main() :
    #Pregunta al usuario la cantidad de boletos que quiere comprar
    boletosA = int (input("Número de boletos de clase A: "))
    boletosB = int (input("Número de boletos de clase B: "))
    boletosC = int (input("Número de boletos de clase C: "))
    #A la variable costoTotal le asigna el valor de la función calcularCosto
    costoTotal = calcularCosto (boletosA, boletosB, boletosC)
    #Imprime el costo total con 2 decimales
    print ("El costo total es: $",format(costoTotal, ".2f"))

main() #llamado de la función