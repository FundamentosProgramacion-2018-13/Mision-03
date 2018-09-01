#Autor: Arturo Márquez Olivar. A01376086
#Calcula el área y perímetro de un trapecio isósceles.

#Función para calcular el área del trapecio.
def calcularArea(baseMayor, baseMenor, altura):
    area= ((baseMayor + baseMenor)/2) * altura
    return area

#Función para calcular el perímetro del trapecio.
def calcularPerimetro(baseMayor, baseMenor, altura):
    ladoPequeño= baseMayor - baseMenor
    hipotenusa= ( (ladoPequeño**2) + (altura**2) )**.5
    
    perimetro= baseMayor + baseMenor + 2*hipotenusa
    return perimetro

#Es la función principal, donde se leen los datos y se imprimen
def main():
    baseMayor= int(input("¿Cuál es la medida de la base mayor del trapecio?"))
    baseMenor= int(input("¿Cuál es la medida de la base menor del trapecio?"))
    altura= int(input("¿Cuál es la medida de la altura del trapecio?"))
    
    area= calcularArea(baseMayor, baseMenor, altura)
    perimetro= calcularPerimetro(baseMayor, baseMenor, altura)
    
    print("El área del trapecio es de %.2f" % (area))
    print("El períetro del trapecio es de %.2f" % (perimetro))
    
#Llamada a la función principal.
main()
    
