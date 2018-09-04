def calcularArea(basemenor, basemayor, altura):
    area = (((basemayor + basemenor)*altura))/2

    return area

def calcularPerimetro(basemenor, basemayor, altura):
    basetriangulo = (basemayor - basemenor)/2
    lado = (basetriangulo**2 + altura**2)**.5

    perimetro = basemenor + basemayor + lado*2

    return perimetro

def main():
    basemenor = int(input("Valor de la base menor: "))
    basemayor = int(input("Valor de la base mayor: "))
    altura = int(input("Valor de la altura: "))

    area = calcularArea(basemenor, basemayor, altura)
    perimetro = calcularPerimetro(basemenor, basemayor, altura)

    print("El valor del area es: %.2f" % area)
    print("El valor del perimetro es: %.2f" % perimetro)

main()

