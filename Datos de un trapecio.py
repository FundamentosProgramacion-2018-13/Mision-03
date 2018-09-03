# Autor: Humberto Carrillo Gómez
# Descripción: Este programa calcula el Area y perímetro de un trapecio utilizando funciones

# Recibe baseMayor, baseMenor y altura para proceder a calcular los lados oblicuos(Hipotenusa)


def calcularHipotenusa(baseMayor, baseMenor, altura):
    catetoA = (baseMayor-baseMenor)/2
    hipotenusa = ((catetoA**2+ altura**2)**(1/2))
    return hipotenusa

# Recibe baseMayor,baseMenor e hipotenusa y después, procede a calcular el perímetro.


def calcularPerimetro (baseMayor, baseMenor, hipotenusa):
    perimetro = baseMayor+baseMenor+2*hipotenusa
    return perimetro

# Recibe baseMayor, baseMenor y altura y utiliza estos valores para calcular el área.


def calcularArea (baseMayor, baseMenor, altura):

    area = (baseMayor+baseMenor)/2*altura
    return area

# Función principal, incorpora a las funciones anteriormente creadas para resolver el problema e imprime las salidas.


def main():
    baseMayor= int(input("Tecleé la base mayor: "))
    baseMenor = int(input("Tecleé la base menor: "))
    altura= int(input("Tecleé la altura: "))
    hipotenusa= calcularHipotenusa(baseMayor,baseMenor,altura)
    perimetro= calcularPerimetro(baseMayor,baseMenor,hipotenusa)
    area= calcularArea(baseMayor,baseMenor,altura)
    print("Área: %.2f" % area)
    print("Perímetro: %.2f" %perimetro)


# LLama a la función principal

main()