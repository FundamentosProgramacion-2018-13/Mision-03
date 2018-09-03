#Autor: Michelle Sánchez Guerrero
#Descripción: Programa que calcula el área y perímetro de un trapecio isósceles.

#Función que calcula el área del trapecio
def calcularArea(baseMayor, baseMenor, altura):
    area = (baseMayor + baseMenor) / 2 * altura
    return area

#Función que calcula el perímetro del trapecio
def calcularPerimetro(baseMayor, baseMenor, altura):
    lado = ((altura ** 2) + ((baseMayor - baseMenor) / 2) ** 2) ** 0.5
    perimetro = baseMayor + baseMenor + lado * 2
    return perimetro

#Función principal. Lee datos e imprime resultados
def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    area = calcularArea(baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    print("Área: %.2f" % (area))
    print("Perímetro: %.2f" % (perimetro))

#Llamar a la función principal
main()