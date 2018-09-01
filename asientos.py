#Autor: Arturo Márquez Olivar. A01376086
#Calcula el total a pagar dependiendo de la cantidad y la clase de boletos que quieras comprar para un evento.

#Calcula el total a pagar.
def calcularPago(asientosA, asientosB, asientosC):
    asientosA= asientosA * 925
    asientosB= asientosB * 775
    asientosC= asientosC * 360
    
    totalPago= asientosA + asientosB + asientosC
    return totalPago

#Función principal que recibe los datos y los imprime.
def main():
    numeroBoletosA = int (input("¿Cuántos asientos clase A compraste?"))
    numeroBoletosB = int (input("¿Cuántos asientos clase B compraste?"))
    numeroBoletosC = int (input("¿Cuántos asientos clase C compraste?"))
    
    
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El total que deberás pagar es de %.2f pesos" % (totalPago))

#Llamada a la función principal.
main()
