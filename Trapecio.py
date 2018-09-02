#Irma Gómez Carmona, A01747743
#Calcular areas y perimetro de un trapecio

def calcularArea(baseMayor, baseMenor, altura):
    areaT=(baseMayor+baseMenor)/2*altura
    return areaT

def calcularPerimetro (baseMayor, baseMenor, altura):
    ladosDiagonales=(((baseMayor-baseMenor)/2)**2+altura**2)**0.5*2
    perimetroT= baseMayor+baseMenor+ladosDiagonales
    return perimetroT

def main ():
    baseMayor=float(input("Escribe la longitud de la base mayor: "))
    baseMenor = float(input("Escribe la longitud de la base menor: "))
    altura = float(input("Escribe la altura: "))
    area=calcularArea(baseMayor,baseMenor,altura)
    perimetro=calcularPerimetro(baseMayor,baseMenor,altura)
    print("Área: %.2f"%(area))
    print("Perimetro: %.2f"%(perimetro))

main ()