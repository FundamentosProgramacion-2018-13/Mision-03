#Autor: Samantha MArtínez Franco A01747686
#Descripción: Calcular area y perimetro de un trapecio
import math


def calcularArea(baseMayor,baseMenor,altura):       #función que calcula el area
    area=((baseMayor+baseMenor)/2)*altura
    return area

def calcularPerimetro(baseMayor, baseMenor, altura):     #función que calcula el perimetro
    lado=(((baseMayor-baseMenor)/2)**2+altura**2)**.5
    perimetro=baseMenor+baseMayor+lado+lado
    return perimetro


def main():      #función principal
    baseMayor= int(input("Escribe la longitud de la base mayor: "))    #pide valores
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    area=calcularArea(baseMayor,baseMenor,altura)                      #valor de area
    perimetro=calcularPerimetro(baseMenor,baseMayor,altura)            #valor de perimetro
    print("Area: %.2f " % (area))                                     #imprimir resultados
    print("Perímetro: %.2f" %(perimetro))

#llamar funcion principal
main()