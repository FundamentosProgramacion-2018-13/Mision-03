#Autor: Alejandro Torices Oliva
#Es un programa que lee las dimensiones de un trapecio isóceles y regresa el perímetro y el área.

#Calcula el área del trapecio al introducir las bases y la altura, usa una fórmula.
def calcularArea(baseMayor, baseMenor, altura):
    area = ((baseMayor + baseMenor) / 2) * altura
    return area

#Calcula el perímetro del trapecio al sumar las bases y las dos hipotenusas que se forman
#en los triángulos exteriores.
def calcularPerimetro(baseMayor, baseMenor, altura):
    hipotenusa = ((((baseMayor - baseMenor) / 2)**2) + (altura**2)) ** .5
    perimetro = baseMayor + baseMenor + (2 * hipotenusa)
    return perimetro

#Es la función principal, obtiene los datos e imprime las soluciones.
def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    area = calcularArea(baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    print("Área: %.2f" % area)
    print("Perímetro: %.2f" % perimetro)

main()