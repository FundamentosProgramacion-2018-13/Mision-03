# Autor: Roberto Emmanuel González Muñoz
# Escribe un programa que lea la base mayor, la base menor y la altura de un trapecio isósceles y que imprima
# Area y Perímetro

def areaTrapecio(basemayor, basemenor, altura):
    areaTrap = ((basemayor + basemenor) / 2) * altura
    return areaTrap


def perimetroDeTrapecio(basemayor, basemenor, altura):
    ladoFaltante = ((altura ** 2) + ((basemayor - basemenor) / 2)) ** 1 / 2
    perimetroTrap = basemayor + basemenor + 2 * ladoFaltante
    return perimetroTrap


def main():
    baseMayor = input(int("Escribe la longitud de la base mayor: "))
    baseMenor = input(int("Escribe la longitud de la base menor: "))
    altura = input(int("Escribe la altura: "))
    perimetro = perimetroDeTrapecio(baseMayor, baseMenor, altura)
    area = areaTrapecio(baseMenor, baseMenor, altura)
    print("El perímetro del trapecio es: %.2f" % perimetro)
    print("El area del trapecio es: %.2f" % area)


main()
