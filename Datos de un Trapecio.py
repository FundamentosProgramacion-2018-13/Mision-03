"""
Nombre: Alexys Martín Coate Reyes
Martícula: A01746998

Descripción: Calcular el área y perímetro de un trapecio con los datos obtenidos.
"""

#Calcula el área de toda la figura con base en la fórmula
def calcularArea(altura, baseMayor, baseMenor):
    area = altura*(baseMenor + baseMayor)/2
    return area

#Calcula el perímetro sumando las bases y obteniendo los lados del trapecio con teorema de pitágoras
def calcularPerimetro(altura, baseMayor, baseMenor):
    perimetro = baseMayor + baseMenor + (2*(((((baseMayor - baseMenor)*.5)**2) + (altura**2))**.5))
    return perimetro

#Imprime los datos: Base menor y mayor, altura, area y perímetro
def imprimir(baseMenor, baseMayor, altura, area, perimetro):
    print("Base menor: {:.2f}" .format(baseMenor))
    print("Base mayor: {:.2f}".format(baseMayor))
    print("Altura: {:.2f}".format(altura))
    print("Área: {:.2f}".format(area))
    print("Perímetro: {:.2f}".format(perimetro))

#Función principal que engloba toda la serie de pasos para resolver el resultado. También obtiene los datos de entrada.
def main():
    baseMenor = float(input("Escribe la longitud de la base menor: "))
    baseMayor = float(input("Escribe la longitud de la base mayor: "))
    altura = float(input("Escribe la altura: "))
    area = calcularArea(altura, baseMayor, baseMenor)
    perimetro = calcularPerimetro(altura, baseMayor, baseMenor)
    imprimir(baseMenor, baseMayor, altura, area, perimetro)

#Llama a la función principal para que se ejecute
main()