#Rodolfo Anibal Altamirano Sánchez, A01377949
#Se te prpoprciona la base menor, base mayor y altura de un trapecio, y debes de sacar area y perimetro


#Calcula el area del trapecio
def calcularArea(baseMayor, baseMenor, altura):
    area = ((baseMayor + baseMenor)*altura)/2
    return area


#Calcula el valor de los laterales para poder sacar perimetro
def calcularLaterales(baseMayor, baseMenor, altura):
    lateral = (((baseMayor-baseMenor)/2)+altura)**0.5
    return lateral


#Suma todos los lados para tener el perimetro
def calcularPerimetro(baseMayor, baseMenor, altura):
    lateral = calcularArea(baseMayor, baseMenor, altura)
    perimetro = (2*lateral)+baseMayor+baseMenor
    return perimetro


#Se llaman todas las funciones
def main():
    #Se pide alura, base mayor y base menor
    baseMayor = float(input("Escribe la longitud de la base mayor: "))
    baseMenor = float(input("Escribe la longitud de la base menor: "))
    altura = float(input("Escribe la altura: "))
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    area = calcularArea(baseMayor, baseMenor, altura)

    #imprime todos los valores
    print("Area: %.2f" % perimetro)
    print("Perimetro: %.2f" % area)



main()
