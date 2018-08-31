# Autor: Silvia Ferman Muñoz
# Programa que lee las medidas de un trapecio isósceles y que imprime el área y perímetro.
# Demo Top-Down


# Se calcula el area del trapecio utilizando una formula
def calcularArea(baseMayor, basemenor, altura):
    area = ((baseMayor + basemenor) / 2) * altura
    return area


# Calcular las hipotenusas de los dos triangulos que se forman en el trapecio
# Calcula el perimetro del trapecio utlizando la hipotenusas
def calcularPerimetro(baseMayor, basemenor, altura):
    hipotenusa = ((((baseMayor - basemenor) / 2)**2) + altura**2) ** 0.5
    perimetro = baseMayor + basemenor + (hipotenusa * 2)
    return perimetro


# Funcion principal donde pregunta las medidas del trapecio y se imprime el resultado
def main():
    baseMayor = int(input("Escribe la longitud de la base Mayor:"))
    basemenor = int(input("Escribe la longitud de la base menor:"))
    altura = int(input("Escribe la altura:"))
    area = calcularArea(baseMayor, basemenor, altura)
    perimetro = calcularPerimetro(baseMayor, basemenor, altura)
    print("Área: %.2f" % area)
    print("Perímetro: %.2f" % perimetro)


# Llama a la funcion principal
main()