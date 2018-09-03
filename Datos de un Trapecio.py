# Autor: Juan Carlos Flores García, A01376511

# Descripción: Programa que calcula el área y perímetro de un trapecio.


# La siguiente función calcula el área del trapecio.
def calcularArea(baseMayor, baseMenor, altura):
    area = ((baseMayor + baseMenor)/2) * altura
    return area


# La siguiente función calcula el perímetro del trapecio.
def calcularPerimetro(baseMayor, baseMenor, altura):
    hipotenusa = ((((baseMayor - baseMenor) / 2) ** 2) + (altura ** 2)) ** .5
    perimetro = (2 * hipotenusa) + baseMayor + baseMenor
    return perimetro


# La siguiente función imprime el área y el perímetro del trapecio.
def imprimir(area, perimetro):
    print("Área: %.2f" % area)
    print("Perímetro: %.2f" % perimetro)


# La función principal lee el valor de la base menor, la base mayor y la altura.
# También calcula el área y perímetro del trapecio e imprime los resultados usando sus respectivas funciones.
def main():
    baseMayor = float(input("Escribe la longitud de la base mayor: "))
    baseMenor = float(input("Escribe la longitud de la base menor: "))
    altura = float(input("Escribe la altura: "))
    area = calcularArea(baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    imprimir(area, perimetro)



# Llama a la función main.
main()