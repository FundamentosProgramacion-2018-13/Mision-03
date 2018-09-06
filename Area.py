# Alex Fernando Leyva Martinez / A01747078
# Calcular el área y perimetro del trapecio

#Permite calcular el área de la figura
def area(baseMayor, baseMenor, altura):
    areaFigura = ((baseMayor + baseMenor)/2) * altura
    return areaFigura

#Permite calcular el perimetro de la figura
def perimetro(baseMayor, baseMenor, altura):
    ladoIndividual = ((baseMayor - baseMenor) / 2)
    lado = (ladoIndividual ** 2 + altura ** 2) ** 0.5
    perimetroFigura = baseMenor + baseMayor + 2*lado
    return perimetroFigura

#Pregunta los datos y llama a las funciones anteriores
def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    areaFigura = area(baseMayor, baseMenor, altura)
    perimetroFigura = perimetro(baseMenor, baseMayor, altura)
    print("Área: %.2f" % area)
    print("Perímetro: %.2f" % perimetro)

main()
