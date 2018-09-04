# David Isaí López Jaimes     A01748363
# Calcula los datos de un trapecio, area y perímetro

# Calcula el área
def calcularArea(baseMayor, baseMenor, altura):
    area = baseMayor + baseMenor
    area = area / 2
    area = area * altura
    return area

def calcularPerimetro(baseMayor, baseMenor, altura):
    perimetro = baseMayor / 4
    perimetro = perimetro ** 2
    perimetro = perimetro + altura ** 2
    perimetro = perimetro ** 0.5
    perimetro = perimetro * 2 + baseMayor + baseMenor
    return perimetro

def main():
    lonitudMayor = int(input("Eescribe la longitud de la base mayor: "))
    lonitudMenor = int(input("Eescribe la longitud de la base menor: "))
    lonitudAltura = int(input("Eescribe la altura: "))

    areaTotal = calcularArea(lonitudMayor, lonitudMenor, lonitudAltura)
    print("Área: ",format(areaTotal, ".2f"))

    perimetroTotal = calcularPerimetro(lonitudMayor, lonitudMenor, lonitudAltura)
    print("Perímetro: ",format(perimetroTotal, ".2f"))

main()
