# Autor:Jesús Emmanuel Alcalá Nava
# Descripcion: calcula el área y perimetro de un trapecio
def calcularArea(baseMayor, baseMenor, altura):
    area = ((baseMayor + baseMenor) * altura) / 2 #formula del área del trapecio
    return area
def calcularCateto(baseMayor, baseMenor, altura):
    baseTriangulo = (baseMayor - baseMenor) / 2
    catetoCuadrado = (altura**2) + ((baseTriangulo)**2) #formula para obtener el cateto con la hipotenusa
    cateto = catetoCuadrado ** (1/2)
    return cateto
def calcularPerimetro(baseMayor, baseMenor, altura):
    cateto = calcularCateto(baseMayor, baseMenor, altura)
    perimetro = baseMayor + baseMenor + cateto * 2 #formula para calcular el perímetro
    return perimetro
def main():
    baseMayor = int(input("Cuál es la longitud de la base mayor? "))
    baseMenor = int(input("Cuál es la longitud de la base menor? "))
    altura = int(input("Cuál es la altura?: "))
    area = calcularArea(baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    print("Área: %.2f Perímetro: %.2f" % (area, perimetro))
main()