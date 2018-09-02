# Autor: Oscar Macias Rodríguez
# Descripción: Programa que lee datos e imprime área y perímetro.

# Calcula el área del trapecio.
def area(baseMayor, baseMenor, altura):
    area = (baseMayor+baseMenor)/2*altura
    return area

# Calcula el perímetro del trapecio.
def perimetro(baseMayor, baseMenor, altura):
    lado = (baseMayor-baseMenor)/2
    lado1 = (lado**2 + altura**2)**.5
    perimetro = baseMayor + baseMenor + 2*lado1
    return perimetro

# Imprime en pantalla el área y el perímetro.
def main():
    baseMayor = int(input("Escribe la longitud de la base mayor:"))
    baseMenor = int(input("Escribe la longitud de la base menor:"))
    altura = int(input("Escribe la altura:"))

    area(baseMayor, baseMenor, altura)
    perimetro(baseMayor, baseMenor, altura)

    print("Área:", "%.2f" % area(baseMayor, baseMenor, altura))
    print("Perímetro:", "%.2f" % perimetro(baseMayor, baseMenor, altura))


main()


