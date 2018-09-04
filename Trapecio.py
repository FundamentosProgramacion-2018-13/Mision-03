#Autor: Daniel Cordova Bermudez
#Descripción: En este programa calcula el precio total de los asientos clase A,B y C.


def calcularArea(longitudBasemayor, longitudBasemenor, altura):
    area= ((longitudBasemayor+longitudBasemenor)/2)*altura
    return area


def calcularPerimetro(Basemayor, Basemenor, altura):
    hipotenusa = (altura**2+((Basemayor-Basemenor)/2)**2)**0.5
    perimetro = hipotenusa*2 + Basemayor + Basemenor
    return perimetro


def main():
    longitudBasemayor = int(input("Escribe la longitud de la base mayor:"))
    longitudBasemenor = int(input("Escribe la longitud de la base menor:"))
    altura = int(input("Escribe la altura:"))

    area = calcularArea(longitudBasemayor,longitudBasemenor,altura)
    perimetro = calcularPerimetro(longitudBasemayor,longitudBasemenor,altura)
    print("Área: %.2f" % area)
    print("Perimetro: %.2f" % perimetro)

main()