#Jesús Roberto Herrera Vieyra // A01377230
#Calcular perímetro y área de un trapecio

#función para calcular el área del trapecio
def calcularArea(B,b,h):
    area = ((B+b)*h)/2
    return area

#función para calcular el perímetro del trapecio
def calcularPerimetro(B,b,h):
    perimetro = B+b+2*(((((B-b)/2)**2+h**2)**0.5))

    return perimetro

#función principal
def main():
    baseMayor=int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la longitud de la altura: "))

    area = calcularArea(baseMayor,baseMenor,altura)
    perimetro = calcularPerimetro(baseMayor,baseMenor,altura)

    print("Área: ""{0:.2f}".format(area))
    print("Perímetro: ""{0:.2f}".format(perimetro))

main()