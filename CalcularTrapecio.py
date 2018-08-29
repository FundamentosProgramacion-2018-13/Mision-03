# Author: Ivan Honc Ayón     A01376466       Grupo 2
# Descripción: Este programa calcula el perímetro y el área de un trapecio.


#Esta función  calcula los catetos de los triángulos que empiezan donde termina la base menor para luego sumar todos los lados y las bases para sacar el perimetro.
def calcularPerimetro(baseMayor, baseMenor, altura):
    ladoTriangulo = (baseMayor-baseMenor)/2
    hipotenusa = ((ladoTriangulo**2)+(altura**2))**(1/2)
    perimetro = baseMayor + baseMenor + (hipotenusa*2)

    return perimetro


#Esta función realiza la suma de las bases, la divide entre dos y luego la multiplica por la altura para sacar el área del trapecio.
def calcularArea(baseMayor, baseMenor, altura):
    area = altura * ((baseMayor + baseMenor)/2)

    return area


#Esta es la función principal para recibir los valores del usuario y llamar al resto de las funciones.
def main():
    bMayor = float(input("Escribe la longitud de la base mayor: "))
    bMenor = float(input("Escribe la longitud de la base menor: "))
    alt = float(input("Escribe la altura: "))
    peri = calcularPerimetro(bMayor, bMenor, alt)
    are = calcularArea(bMayor, bMenor, alt)
    print("Área: %.2f" % are)
    print("Perímetro: %.2f" % peri)


main()
