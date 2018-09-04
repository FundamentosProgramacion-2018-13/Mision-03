# Autor: Oscar Alejandro Torres Maya, A01377686, grupo 04
# Descripción: Programa que calcula el área y perímetro del trapecio isóceles

#Función para calcular el area del trapecio
def areaTrapecio (baseMayor, baseMenor, altura):
    area = ((baseMayor+baseMenor)/(2))*altura
    return area

#Funcion para calcular perímetro del trapecio
def perimetroTrapecio (baseMayor,baseMenor, altura):
    catetoAdyacente = (baseMayor-baseMenor)/2
    hipotenusa = ((altura**2+ catetoAdyacente**2)**(1/2))
    perimetro = baseMayor + baseMenor + hipotenusa*2
    return perimetro

# Función principal, lee datos e imprime datos
def main():
    baseMayor = float(input("Escribe la longitud de la base mayor: "))
    baseMenor = float(input("Escribe la longitud de la base menor: "))
    altura = float(input("Escribe la altura: "))
    perimetro = perimetroTrapecio (baseMayor,baseMenor, altura)
    area = areaTrapecio (baseMayor, baseMenor, altura)
    print("Área: %0.2f" % (area))
    print("Perímetro: %0.2f" % (perimetro))

main()