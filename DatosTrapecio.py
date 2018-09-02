#Luis Jonathan Rosas Ramos
# A01377942
# Calcula el area y perimtro de un trapecio

import math

#Para calcular el area necesitas utilizar la formaula, por lo que la traducimos a un leguaje que pyhon entienda
def calcularArea(baseMayor,baseMenor, altura):
    area = ((baseMayor+baseMenor)*altura)/2
    return area

def calcularPerimetro(baseMayor,baseMenor,altura):
    # para obtener la base de solo el triangulo, restamos la base menor de la mayor y como saldrian los dos lados
    # lo divimos entre 2
    c = (baseMayor-baseMenor)/2
    # sabemos que la hipotenusa de un triangulo es igual a la raiz del cuadrado de los catetos
    lado = math.sqrt((altura**2)+(c**2))
    perimetro = (baseMenor+baseMayor+(lado*2))
    return perimetro

def main():
    # preuntar la base mayor, menor y la altura.
    baseMayor = int(input("Ingresa la base mayor: "))
    baseMenor = int(input("Ingresa la base menor: "))
    altura = int(input("Ingresa la altura: "))
    # calcular area y perimetro con los datos dados.
    area = calcularArea(baseMayor,baseMenor, altura)
    perimetro = calcularPerimetro(baseMenor,baseMayor, altura)
    # imprimir los resultados
    print("Area: %.2f" %area)
    print("Perimetro: %.2f"%perimetro)

# Llamar a la funcion principal
main()