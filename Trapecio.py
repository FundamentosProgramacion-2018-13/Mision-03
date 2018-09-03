# Autor: Jonathan Sanabria Rocha
# Sacar area y perimetro de un trapecio isoceles

import math
def calcularArea(basemayor,basemenor,altura):
    area = (basemayor + basemenor) / 2 * altura
    return area
#Calcula el area con los valores dados por el usuario.

def calcularPeimetro(basemayor,basemenor,altura):
    ladooblicuo = (basemayor - basemenor)/2
    pitagorasoblicuo = math.sqrt(ladooblicuo**2+altura**2)
    perimetro = 2*pitagorasoblicuo + basemayor + basemenor
    return perimetro
#Calcula el perimetro, primero busca el valor de uno de los dos lados oblicuos,
#para despues operarlo en la formula para sacar el perimetro.

def main():
    basemayor = int(input("Escribe la longitud de la base mayor: "))
    basemenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    area = calcularArea(basemayor,basemenor,altura)
    perimetro = calcularPeimetro(basemayor,basemenor,altura)

    print("Area: %.2f" % area)
    print("Perimetro: %.2f" % perimetro)

main()
