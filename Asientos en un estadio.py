# Autor: Carlos Alberto Reyes Ortiz
# Cuanto tienes que pagar por los asientos

def calcularPago(asientosA, asientosB, asientosC): #Calcula el total a pagar por todos los asientos
    costoAsientosA = asientosA * 925
    costoAsientosB = asientosB * 775
    costoAsientosC = asientosC * 360
    totalPago = costoAsientosA + costoAsientosB + costoAsientosC
    return totalPago



def main(): #Función principal: da la suma de los costos de todos los asientos. 
    asientosA = int(input("Número de boletos de clase A: "))
    asientosB = int(input("Número de boletos de clase B: "))
    asientosC = int(input("Número de boletos de clase C: "))
    totalPago = calcularPago(asientosA, asientosB, asientosC)

    print("El costo total es: $%.2f" %(totalPago))





#Llamar funciones

main()
