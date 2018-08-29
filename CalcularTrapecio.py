# Author: Ivan Honc Ayón     A01376466       Grupo 2
# Descripción: Este programa calcula el perímetro y el área de un trapecio.


def calcularPerimetro(baseMayor, baseMenor, altura):
    ladoTriangulo = (baseMayor-baseMenor)/2
    hipotenusa = ((ladoTriangulo**2)+(altura**2))**(1/2)
    perimetro = baseMayor + baseMenor + (hipotenusa*2)

    return perimetro


def calcularArea(baseMayor, baseMenor, altura):
    area = altura * ((baseMayor + baseMenor)/2)

    return area


def main():
    bMayor = float(input("Escribe la longitud de la base mayor: "))
    bMenor = float(input("Escribe la longitud de la base menor: "))
    alt = float(input("Escribe la altura: "))
    peri = calcularPerimetro(bMayor, bMenor, alt)
    are = calcularArea(bMayor, bMenor, alt)
    print("Área: %.2f" % are)
    print("Perímetro: %.2f" % peri)


main()