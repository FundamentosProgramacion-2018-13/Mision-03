# Autor: Luis Armando Miranda Alcocer
# Lee la base mayor y menor de un trapecio y calcula su área y perímetro

def calcularArea (baseMayor, baseMenor, altura):
    area = ((baseMayor + baseMenor)/2)*altura
    return area

def calcularPerimetro(baseMayor, baseMenor, altura):
    hipotenusaCuadrada = (((baseMayor - baseMenor)/2)**2) + altura**2 #Se Calcula hipotenusa al cuadrado
    hipotenusa = (hipotenusaCuadrada)**(1/2) #Se saca la raíz de la hipotenusa al cuadrado para calcular la hipotenusa
    perimetro = (baseMayor + baseMenor + (2* hipotenusa)) #Se suman los lados para obtener el perímetro
    return perimetro

def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    area = calcularArea(baseMayor, baseMenor, altura) #Llama a la función calcularArea
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura) #Llama a la función calcularPerimetro
    print ("Área: %.2f" %(area)) #Dos decimales
    print("Perímetro: %.2f" %(perimetro))

main()