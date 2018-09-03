#Autor: David Rodriguez
#Calcula el área y el perímetro de un trapecio isóceles
#En base a la longitus de la base mayor de la base menor



#Calcula el perímetro del trapecio haciendo uso de la base mayor, la base menor,
#la altura y el teorema de pitágoras (a^2+b^2=c^2)
def calcularPerimetro(altura, baseMayor, baseMenor):
    ladoTriangulo = (baseMayor-baseMenor)/2
    ladoTrapecio = ((altura**2)+(ladoTriangulo**2))**0.5
    perimetro = (ladoTrapecio*2) + baseMenor + baseMayor
    return perimetro


#Calcula el área del trapecio con la fórmula A=((B+b)/2)*h
def calcularArea(baseMayor, baseMenor, altura):
    area = ((baseMayor+baseMenor)/2)*(altura)
    return area

#Imprime el área y el perímetro
def imprimir(area, perimetro):
    print("Área: %.2f" % (area))
    print("Perímetro: %.2f" % (perimetro))


def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    area = calcularArea(baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(altura, baseMenor, baseMayor)
    imprimir(area, perimetro)

#Llama a la función principal
main()

