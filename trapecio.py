#Jocelyn López Ortíz A01377451
#Cálculo de área y perímetro de in trapecio isósceles

def calcularArea(baseMa, baseMe, altura):
    area = ((baseMa + baseMe)/2)*altura
    return area

def calcularperimetro(baseMa, baseMe, altura):
    hipotenusa = (altura**2 + ((baseMa-baseMe)/2)**2)**0.5
    perimetro = baseMa + baseMe + hipotenusa*2
    return perimetro

def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    area = calcularArea(baseMayor, baseMenor, altura)
    perimetro = calcularperimetro(baseMayor, baseMenor, altura)
    print ("Área: %.2f" %(area))
    print ("Perímetro: %.2f" %(perimetro))

main()