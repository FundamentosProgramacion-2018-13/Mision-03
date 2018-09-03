# Autor: Zoe Caballero Dominguez Matrícula: A01747247
# Descripción: Lee la base mayor, la mase menor y la altura de un trapecio isósceles y calcula el área y perímetro

# Programa

# Función calcularArea hace la operación para obtener el area del trapecio y regresa a main el resultado
def calcularArea (baseMayor, baseMenor, altura):
    area = (baseMayor + baseMenor) / 2 * altura
    return area


#Función calcularPerímetro saca el lado del trapecio con el teorema de pitágoras y calcula el perimetro del trapecio, regresando el resultado a main"""
def calcularPerimetro (baseMayor, baseMenor, altura):
    baseTriangulo = (baseMayor - baseMenor) / 2
    ladoTrapecio = ((altura ** 2) + (baseTriangulo ** 2)) ** 0.5
    perimetro = (ladoTrapecio * 2) + baseMenor + baseMayor
    return perimetro


# Función main lee los datos del trapecio, llama a las funciones calcularArea y calcularTrapecio e imprime el área y perímetros del mismo.
def main ():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura:  "))
    areaTrapecio = calcularArea (baseMayor, baseMenor, altura)
    perimetroTrapecio = calcularPerimetro (baseMayor, baseMenor, altura)
    print("Área: %.2f" % (areaTrapecio))
    print("Perímetro: %.2f" % (perimetroTrapecio))


#Llamar a main
main()