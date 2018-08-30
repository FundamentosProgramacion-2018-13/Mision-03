# encoding: UTF-8
# Autor: Diego Palmerin Bonada, A01747290
# Descripcion: Calcula el perímetro y el área de un trapecio isóceles preguntando base mayor, menor y altura

"""
Análisis:
E: baseMayor. baseMenor, altura
S: perimetro, area
E/S:
perimetro:
calculoHipotenusas=2*((((baseMayor-baseMenor)/2)**2)+altura**2)**0.5
perimetro= (baseMayor+baseMenor)+calculoHipotenusas

area:
areaRectangular = b*h
areaTriangulos = ((B-b)*h)/2
areaTotal = areaRectangular+areaTriangulos


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

def calcularPerimetro(B,b,h):
    #calcular largo de las dos hipotenusas
    calculoHipotenusas = 2*(((((B - b) / 2) ** 2) + h ** 2) ** 0.5)
    #Sumar largo de hipotenusas
    perimetroTotal = (B + b) + calculoHipotenusas
    return(perimetroTotal)


def calcularArea(B,b,h):
    areaTotal = ((B+b)/2)*h
    return (areaTotal)


def main():
    #preguntar al usuario los largos
    baseMayor = float(input("Escribe la longitud de la base mayor: "))
    baseMenor = float(input("Escribe la longitud de la base menor: "))
    altura = float(input("Escribe la altura: "))
    #imprimir los resultados llamado a las funciones que los calculan
    print("Área: %.2f" % (calcularArea(baseMayor,baseMenor,altura)))
    print("Perímetro: %.2f" % (calcularPerimetro(baseMayor, baseMenor, altura)))

#Llamar la función main
main()