#Autor Claudio Mayoral García
#Descripción: El programa leera la base mayor, la base menor y la altura de un trapecio isóceles e imprimirá el área y perímetro



def calcularArea(baseMayor, baseMenor, altura):
    # Calcula el area con baseMayor, baseMenor y la altura
    # Regresa el area
    area = ((baseMayor + baseMenor)/2) * altura
    return area


def calcularPerimetro(baseMayor, baseMenor, altura):
    # Calcula la hipotenusa con la base menor y mayor usando una formula
    # Calcula el perimetro del trapecio con la hipotenusa, la base menor y la base mayor
    # Regresa el perímetro
    hipotenusa = ((((baseMayor - baseMenor) / 2) ** 2) + (altura ** 2)) ** .5
    perimetro = baseMayor + baseMenor + (2 * hipotenusa)
    return perimetro


def main():
    # baseMayor = Leer la longitud de la base mayor
    # baseMenor = Leer la longitud de la base menor
    # altura = Leer la altura del trapecio
    # Calcula el área y el perímetro con las funciones calcularArea y calcularPerimetro
    # Imprime los resultados
    baseMayor = float(input("Escribe la longitud de la base mayor: "))
    baseMenor = float(input("Escribe la longitud de la base menor: "))
    altura = float(input("Escribe la altura: "))
    area = calcularArea(baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    print("Área: %.2f" % area)
    print("Perímetro: %.2f" % perimetro)


#Llama a la función "main"
main()
