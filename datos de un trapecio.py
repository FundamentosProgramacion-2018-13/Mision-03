# Autor: Rubén Villalpando Bremont
# El programa saca el área y perímetro de un trapecio a partir de la base mayor, base menor, y la alura.

# Esta función saca el área del trapecio
def areaTrapecio(alturaTrapecio, baseMenorTrapecio, baseMayorTrapecio):
    area = ((baseMenorTrapecio + baseMayorTrapecio)/2)*alturaTrapecio
    return area


# Esta función calcula el perímetro del trapecio
def perimetroTrapecio(alturaTrapecio, baseMenorTrapecio, baseMayorTrapecio):
    ladosTrapecio = ((alturaTrapecio**2) + ((baseMayorTrapecio - baseMenorTrapecio)/2)**2)**(1/2)
    perimetro = baseMenorTrapecio + baseMayorTrapecio + ladosTrapecio*2
    return perimetro


# Función main
def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    perimetro = perimetroTrapecio(altura, baseMenor, baseMayor)
    area = areaTrapecio(altura, baseMenor, baseMayor)
    print("Área: %.2f" % (area))
    print("Perímetro: %.2f" % (perimetro))


# Llamar a main
main()


