# Mariana Caballero Cabrera A01376544

# A continuación voy a escribir un programa que calcule el área y perímetro de un trapecio



#esta función calcula el área

def calcularArea (baseMayor,baseMenor, altura):
    area = (baseMayor+baseMenor)*altura/2
    return area



#esta función calcula el perímetro

def calcularPerimetro ( baseMayor,baseMenor, ladotrianguloU):
    perimetro = (ladotrianguloU *2) + baseMayor + baseMenor

    return perimetro



# función para calcular la hipotenusa del triángulo

def calcularLado (baseMayor, altura):
    ladoTriangulo1 = (baseMayor/4)
    ladoTriangulo2 = (ladoTriangulo1**2)+(altura**2)
    ladoTrianguloU = ladoTriangulo2**.5

    return ladoTrianguloU



# está función manda a immprimir

def imprimir (area,perimetro):
    print ("Área: %5.2f"  % (area))
    print("Perímetro: %5.2f" % (perimetro))


# función principal

def main():
    baseMayor = int(input( "Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input( "Escribe la altura: "))

    ladotrianguloU = calcularLado (baseMayor , altura)
    area = calcularArea(baseMayor,baseMenor, altura)
    perimetro = calcularPerimetro ( baseMayor,baseMenor, ladotrianguloU)

    imprimir (area, perimetro)


# llamamos a la función principal
main()
