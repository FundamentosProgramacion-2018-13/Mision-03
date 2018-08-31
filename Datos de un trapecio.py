# Autor: Zabdiel Valentin Garduño Vivanco, A01377950
# Descripcion: sacar el area y perimetro de un trapecio.


def area(baseMayor, baseMenor, altura):
    area=((baseMayor+baseMenor)/2)*altura
    return area

def perimetro(baseMayor, baseMenor, altura):
    catetoAdyacente=(baseMayor-baseMenor)/2
    hipotenusa=(catetoAdyacente**2+altura**2)**(1/2)
    perimetroTotal=hipotenusa+hipotenusa+baseMayor+baseMenor
    return perimetroTotal


def main():
    baseMayor=int(input("Escribe la longitud de la base mayor: "))
    baseMenor=int(input("Escribe la longitud de la base menor: "))
    altura=int(input("Escribe la altura: "))

    areaFigura=area(baseMayor, baseMenor, altura)
    perimetroFigura=perimetro(baseMayor,baseMenor,altura)

    print("Area: %.2f" % (areaFigura))
    print("Perimetro: %.2f" % (perimetroFigura))

main()


