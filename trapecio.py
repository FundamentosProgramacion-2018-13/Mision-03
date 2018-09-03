#encoding: UTF-8
#Autor: Alek Howland, A01747764
#Descripcion: Programa que calcule el area y perimetro de un trapecio isosceles

def calcularArea(baseMayor, baseMenor, altura): #Calcula el area del trapecio
    areatotal = (baseMayor + baseMenor)/ 2 * altura
    return areatotal


def calcularPerimetro(baseMayor, baseMenor, altura): #Calcula el perímetro del trapecio
    baseTria = (baseMayor - baseMenor )/ 2
    hipo = ((altura**2)+(baseTria**2))**0.5
    perimetro = baseMayor + baseMenor + 2 * hipo
    return perimetro


def imprimir(perimetro, areatotal): #Imprime los resultados
    print ("Area: %.2f" % (areatotal))
    print ("Perímetro: %.2f" % (perimetro))



def main(): #Función principal
    baseMayor = float(input("Escribe la longitud de la base mayor: "))
    baseMenor = float(input("Escribe la longitud de la base menor: "))
    altura = float(input("Escribe la altura: "))
    calcularArea(baseMayor, baseMenor, altura)
    calcularPerimetro(baseMayor, baseMenor, altura)
    imprimir(calcularPerimetro(baseMenor, baseMayor, altura), calcularArea(baseMayor, baseMenor, altura))

main() #Se llama a la función principal




