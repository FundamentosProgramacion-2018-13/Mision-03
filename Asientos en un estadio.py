# Autor: Humberto Carrillo Gómez
# Descripción: Este programa calcula el costo de asientos en un estadio por medio de funciones.


# Recibe el número de asientos en cada clase y regresa el pago total.
def calcularPago(asientosA, asientosB, asientosC):
    totalPago= asientosA*925+asientosB*775+asientosC*360
    return totalPago

# Función principal, resuelve el problema e imprime salidas.


def main():


    asientosA= int(input("Teclea el número de asientos de la clase A: ")) #Pregunta al usuario por el número de asientos
    asientosB= int(input("Teclea el número de asientos de la clase B: "))
    asientosC= int(input("Teclea el número de asientos de la clase C: "))
    totalPago= calcularPago(asientosA,asientosB,asientosC)     # Utiliza a la función calcularPago para obtener el costo

    print("El costo total es: $%.2f" %(totalPago))                      # Muestra el costo total con centavos


# Llama a la función principal
main()