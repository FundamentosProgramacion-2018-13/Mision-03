#Autor: Víctor Manuel Rodríguez Loyola  A01747755
#Descripción: Este programa calcula el área y perímetro de un trapecio isósceles


def calcularArea(bMenor, bMayor, altura): #Calcula el área del trapecio
    area = ((bMayor+bMenor)/2)*altura
    return area


def calcularPerimetro(bMenor, bMayor, altura): #Calcula el perímetro del trapecio
    hipotenusa = ((((bMayor-bMenor)/2)**2) + (altura**2))**0.5
    perimetro = bMenor+bMayor + (2*hipotenusa)
    return perimetro

def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    area= calcularArea(baseMayor,baseMenor, altura)
    perimetro= calcularPerimetro(baseMayor,baseMenor, altura)
    print("Área: %.2f" %(area))
    print("Perímetro: %.2f" %(perimetro))


main()

