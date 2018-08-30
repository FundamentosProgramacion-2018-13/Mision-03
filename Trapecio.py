# Autor: Luis Humberto Burgueño Paz
# Lee la base mayor, la base menor y la altura de un trapecio  e imprime su área y perímetro

# Recibe como parámetros la base menor, la base mayor y la altura para calcular el área total del trapecio
def calcularArea(baseMenor, baseMayor, altura):
   areaCuadrado = baseMenor * altura
   areaTriangulo = (((baseMayor - baseMenor) / 2) * altura) / 2
   areaTotal = areaCuadrado + (2*areaTriangulo)
   return areaTotal

# Recibe como parámetros la base menor, la base menor y la base mayor para cauclar el perímetro del trapecio
def calcularPerimetro(baseMenor, baseMayor, altura):
   hipotenusa = ((((baseMayor - baseMenor) / 2)**2) + (altura**2))**0.5
   perimetroTotal = baseMenor + baseMayor + (2*hipotenusa)
   return perimetroTotal

# Lee la base menor, base mayor y la altura y los envía a calcularArea y calcularPerimetro para imprimir el Área y el Perímetro
def main():
   baseMayor = int(input("Escribe la longitud de la base mayor: "))
   baseMenor = int(input("Escribe la longitud de la base menor: "))
   altura = int(input("Escribe la altura: "))
   area = calcularArea(baseMenor, baseMayor, altura)
   perimetro = calcularPerimetro(baseMenor, baseMayor, altura)
   print("Área: %.02f" % area)
   print("Perímetro: %.02f" % perimetro)


main()
