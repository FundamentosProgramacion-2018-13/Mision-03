# Damián Iván García Ravelo
# A01376354
#Programa que calcula el área y perímetro de un trapecio

#Declarar la función para calcular eel área

def calcularArea (baseMayor, baseMenor, altura):
#Función que usa la baseMayor, baseMenor y altura para calcular área
    area = (baseMayor + baseMenor)/2 * altura
    return area

def calcularPerimetro (baseMayor, baseMenor, altura):
#Función que usa la baseMayor, baseMenor y altura para calcular perímetro
    baseTriangulo = (baseMayor-baseMenor)/2  #Calcular la base del triángulo
    ladoTriangulo = ((baseTriangulo)**2 + (altura)**2)**0.5 #Teorema de pitágoras para el cálculo de la hipotenusa
    perimetro = baseMenor + baseMenor + (baseMayor - baseMenor) + ladoTriangulo + ladoTriangulo #Suma de todos los puntos del trapecio

    return perimetro
def main():
#Pregunta al usuario el valor de la base mayor, la base menor y la altura
    baseMayor = int(input("Escribe la longitud de la baseMayor: "))
    baseMenor = int(input("Escribe la longitud de la baseMenor: "))
    altura = int(input("Escribe la altura: "))
    areaTotal = calcularArea (baseMayor, baseMenor, altura) #Definición del área total
    perimetroTotal = calcularPerimetro (baseMayor, baseMenor, altura) #Definición del perimetro total
    print("Área:", format(areaTotal, ".2f")) #Imprimir el área con 2 decimales
    print("Perímetro: ", format(perimetroTotal, ".2f")) #Imprimir el perímetro con 2 decimales

main() #llamado de la función principal