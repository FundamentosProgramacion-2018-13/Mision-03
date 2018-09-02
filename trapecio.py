# Autor: Alex Serrano Durán
# Este programa calcula el perímetro y el área de un trapecio isósceles


def calcularArea(baseMayor, baseMenor, altura):             # Calcula el área del trapecio
    area = ((baseMayor + baseMenor) * altura) / 2
    return area


def calcularOblicuo(baseMayor, baseMenor, altura):          # Calcula el lado oblicuo del trapecio
    baseTriangulo = (baseMayor - baseMenor) / 2             # Base del triángulo rectángulo que se forma con la altura y el lado oblicuo
    oblicuocuadrado = (altura**2) + ((baseTriangulo)**2)    # Pitágoras, con el lado oblicuo como hipotenusa
    oblicuo = oblicuocuadrado ** (1/2)
    return oblicuo


def calcularPerimetro(baseMayor, baseMenor, altura):        # Calcula el perímetro ya con los lados oblicuos
    oblicuo = calcularOblicuo(baseMayor, baseMenor, altura)
    perimetro = baseMayor + baseMenor + oblicuo * 2
    return perimetro


def main():                     # Función main, pide las medidas e imprime los resultados
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    area = calcularArea(baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    print('''
Área: %.2f
Perímetro: %.2f''' % (area, perimetro))


main()
