# Autor: Luis Ricardo Chagala Cervantes.
# Calcular Área y Perímetro de un trapecio a partir de las medidas de las bases y la altura


# La linea de codigo empieza después de esta linea.

#Se calcula el perimetro del triangulo.
def Triangulo(BaseMayor, BaseMenor, Altura):
    Catetoa = (BaseMayor - BaseMenor) / 2
    Catetob = Altura
    Hipotenusa = (Catetoa **2 + Catetob **2 )** 0.5
    triangulo = Hipotenusa
    return triangulo

#Se calcula el area del trapecio.
def CalcularArea(BaseMayor, BaseMenor, Altura):
    Area = ((BaseMayor + BaseMenor) * Altura) / 2
    return Area

#Se calula el perimetro total del trapecio.
def CalcularPerimetro(BaseMayor, BaseMenor, Altura):
    Perimetro = BaseMayor + BaseMenor + Triangulo(BaseMayor, BaseMenor, Altura) * 2
    return Perimetro


def Impri(Area, Perimetro):
    print("Área: %.2f" % (Area))
    print("Perímetro: %.2f" % (Perimetro))

def Imprimir(BaseMayor, BaseMenor, Altura):
    Area = CalcularArea(BaseMayor, BaseMenor, Altura)
    Perimetro = CalcularPerimetro(BaseMayor, BaseMenor, Altura)
    Impri(Area, Perimetro)


def main():
    BaseMayor = int(input("Longitud de la base mayor: "))
    BaseMenor = int(input("Longitud de la base menor: "))
    Altura = int(input("Altura: "))
    Imprimir(BaseMayor, BaseMenor, Altura)

main()
