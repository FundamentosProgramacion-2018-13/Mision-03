# Autor: Erick David Ramírez Martínez, A01748155, Grupo: 2
# Descripción: Programa para calcular el perímetro y área de un trapecio isosceles de acuerdo a las medidas de la base mayor, la base menor y su altura.


def areaDelTrapecio(baseMayor,baseMenor,altura):
    area = (baseMayor + baseMenor) * altura / 2

    return area


def perimetroDelTrapecio(basemayor,baseMenor,altura):
    catetoAdy = (basemayor-baseMenor) / 2
    lados = 2 * ((altura**2 + catetoAdy**2)**0.5)
    perimetro = basemayor+baseMenor+lados

    return perimetro


def main():
    baseMayor = float(input("Ingrese la medida de la base mayor: "))
    baseMenor = float(input("Ingrese la medida de la base menor: "))
    altura = float(input("Ingrese la medida de la altura: "))

    areaTrap = areaDelTrapecio(baseMayor,baseMenor,altura)
    perimetroTrap = perimetroDelTrapecio(baseMayor,baseMenor,altura)

    print("El área del trapecio es: %0.2f" % (areaTrap))
    print("El perímetro del trapecio es: %0.2f" % (perimetroTrap))


main()
