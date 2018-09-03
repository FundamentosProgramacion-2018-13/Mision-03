# JavierAlexandro Vargas Sánchez A01377718
'''Programa que calcula area y perímetro de un trapecio isósceles'''


def calcularArea(bMay, bMen, altura):  #Calcula área del trapecio
    area = ((bMay + bMen)/2) * altura
    return area


def calcularLado(bMen, bMay, altura): #calcula la longitud de el lado del trapecio
    lado =(((((bMay - bMen)/ 2) ** 2)+(altura ** 2))**.5)
    return  lado


def calcularPerimetro(bMay, bMen, lado):  #calcula el perimetro
    perimetro = (lado * 2) + bMay + bMen
    return  perimetro


def imprimir(area, perimetro):  #Imprime area y perimetro
    print("Área:", format(area, ".2f"))
    print("Perímetro:", format(perimetro, ".2f"))


def main():
    bMay = int(input("Escribe la longitud de la base mayor: "))
    bMen = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    area = calcularArea (bMay,bMen, altura)
    lado = calcularLado (bMen, bMay, altura)
    perimetro =  calcularPerimetro (bMay, bMen, lado)
    imprimir (area, perimetro)

main()