# encoding: UTF-8
# Autor: Diego Palmerin Bonada, A01747290
# Descripcion: Calcula el costo de diferentes boletos

"""
Análisis:
E: asientosA, asientosB, asientosC
S: costoTotal
E/S: (asientosA*925)+(asientosB*775)+(asientosC*360)

Algoritmo:
En la función main:
Preguntar al usuario cuántos boletos para asientos A necesita.
Preguntar al usuario cuántos boletos para asientos B necesita.
Preguntar al usuario cuántos boletos para asientos C necesita.
Ejecutar la función calcularPago con los valores dados por el usuario.
Multiplicar la cantidad de asientos en cada sección por su costo.
Sumar todos los productos y regresar el valor de la sumatoria.
En la función main, reportar al usuario el costo total
"""


def calcularPago(a,b,c):
    #multiplicar cantidad por su costo
    totalPago = (a*925)+(b*775)+(c*360)
    #regresar el valor del costo total a la función main para que la imprima
    return(totalPago)


def main():
    #preguntar cantidad de asientos a usuario
    asientosA = int(input("Número de boletos de clase A: "))
    asientosB = int(input("Número de boletos de clase B: "))
    asientosC = int(input("Número de boletos de clase C: "))
    #Imprimir los resultados
    print("El costo total es: $%.2f" % (calcularPago(asientosA, asientosB, asientosC)))

#Ejecutar la función main
main()