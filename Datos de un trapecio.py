#Joshua Sánchez Martínez A01274269
#Pide al usuario las medidas de un trapecio para dar un area y perimetro

def calcularArea(bMa, bMe, al):

    area = ( (bMa + bMe)/2 )*al

    return area

def calcularPerimetro(bMa, bMe, al):

    #Para conseguir el perimetro se necesita la medida de uno de los lados que posteriormente se multiplica por 2
    #Para esto se usara el teorema de pitágoras

    lado = (   (((bMa-bMe)/2)**2) + ((al)**2) )**.5

    perimetro = 2*(lado) + bMa + bMe

    return perimetro

def main():

    #Los valores a ingresar puden ser flotantes para una mayor precisión de resultados

    baseMayor = float(input("Ingresa la medida de la base mayor del trapecio: "))
    baseMenor = float(input("Ingresa la medida de la base menor del trapecio: "))
    altura = float(input("Ingresa la medida de la altura del trapecio: "))

    area = calcularArea(baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)

    print("Área: %.2f" % area)
    print("Perímetro: %.2f" % perimetro)



main()