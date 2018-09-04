#Autor: Luis Mario Cervantes Ortiz
#Descripción:Calcular el costo totoal de asientos comprados entre 3 tipos de asientos con diferentes costos.

def calcularPago(numAsisentoA, numAsientoB, numAsientoC): #Calcular el costo de cada asiento comprado
    AsientoA=925
    AsientoB=775
    AsientoC=360
    calcularPago=(AsientoA*numAsisentoA+AsientoB*numAsientoB+AsientoC*numAsientoC)
    return calcularPago
def main(): #Preguntar los datos
    numAsientosA= int(input("Número de boletos clase A:"))
    numAsientosB = int(input("Número de boletos clase B:"))
    numAsientosC = int(input("Número de boletos clase C:"))
#Calcular el costo total de los asientos comprados
    costoTotal=calcularPago(numAsientosA,numAsientosB,numAsientosC)
    print("El costo total es: %.2f"%(costoTotal))

main()