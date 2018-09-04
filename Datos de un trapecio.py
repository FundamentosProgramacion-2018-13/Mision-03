#Autor: Carlos Alberto Reyes Ortiz
#Saca Área y perímetro de un trapecio isóceles

def calcularArea(baseMayor, baseMenor, altura):       #Calcula el área del trapecio
    area = ((baseMenor + baseMayor) / 2) * altura
    return area


def calcularPerimetro(baseMayor, baseMenor, altura):    #Calcula el perímetro del trapecio
    ladoCateto = (baseMenor - baseMayor) / 2
    ladoHipotenusa = ( altura**2 + ladoCateto**2 ) ** (1/2) #OJO: es importante poner el 1/2 entre paréntesis
    perimetro = baseMayor + baseMenor + ladoHipotenusa + ladoHipotenusa
    return perimetro



def main():  #Función principal: Da el área y el perímetro de un trapecio isóceles
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura:  "))  #Se puso un espaciador de 2 basado al resultado base del profesor
    area = calcularArea(baseMayor, baseMenor, altura)
    print("Área: %.2f" %(area))
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    print("Perímetro: %.2f" %(perimetro) )



main()
