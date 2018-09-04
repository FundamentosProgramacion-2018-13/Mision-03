# Carlos Badillo García             A01377618
# Programa que lee la base mayor, la base menor y la altura de un trapecio isósceles; también imprime perímetro y área

def calcularArea(longitudBaseMayor, longitudBaseMenor, longitudAltura): #Función que sirve para calcular el área del trapecio
    area = ((longitudBaseMayor + longitudBaseMenor)/2)*longitudAltura
    return area

def calcularPerimetro(longitudBaseMayor, longitudBaseMenor, longitudAltura): #Función que sirve para calcular el perímetro del trapecio
    lado = (longitudBaseMayor - longitudBaseMenor)/2
    hipotenusa = ((longitudAltura**2) + (lado**2))**(1/2)
    perimetro = longitudBaseMayor + longitudBaseMenor + (2*hipotenusa)
    return perimetro

def main(): #Función que sirve para que el usuario introduzca la longitud de la base mayor, la base menor y la altura, además de imprimir el área y el perímetro del trapecio
    longitudBaseMayor = int(input("Escribe la longitud de la base mayor: "))
    longitudBaseMenor = int(input("Escribe la longitud de la base menor: "))
    longitudAltura = int(input("Escribe la altura:  "))
    area = print("Área: %.2f" %calcularArea(longitudBaseMayor, longitudBaseMenor, longitudAltura))
    perimetro = print("Perímetro: %.2f" %calcularPerimetro(longitudBaseMayor, longitudBaseMenor, longitudAltura))

main()