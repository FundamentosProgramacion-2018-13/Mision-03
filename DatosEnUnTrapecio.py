# Emiliano Heredia Garcia A01377072
# Calcula el perímetro y el área de un trapecio dado su base menor, base mayor y altura.

def calcularArea(baseMenor, baseMayor, altura):
    # Calcula el area del trapecio dado la base maneor la base meyor y la altura con la formula:
    # A = (baseMayor+BaseMenor)*(h/2)
    return ((baseMayor+baseMenor)/2)*altura

def calcularPerimetro(baseMenor, baseMayor, altura):
    # Calcula el perimetro de un trapecio. Para esto suma la base mayor la base menor y la altura.
    # Despues calcula las  diagonales. Para esto cada lado lo toma como un triangulo rectangulo
    # (basemayor-base menor) da como resultado la base del triangulo y aplica el teorema de pitagoras.

    hipo = ((((baseMayor-baseMenor)/2)**2)+(altura**2))**.5

    return (baseMenor+baseMayor+2*hipo)

def main():

    baseMayor = int(input("Escriba la longitud de la base mayor: "))
    baseMenor = int(input("Escriba la longitud de la base menor: "))
    altura = int(input("Escriba la altura: "))
    area = calcularArea(baseMenor, baseMayor, altura)
    perimetro = calcularPerimetro(baseMenor, baseMayor, altura)
    print("Área: %.2f "%area)
    print("Perímetro: %.2f"%perimetro)

main()