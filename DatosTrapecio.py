#Autor: Alberto Contreras Torres
#Calcular área y perimetro de un trapcio, segun los datos proporcionados

#Recibe base mayor, menor y altura y regresa area
def calcularArea(baseM, basem, altura):
    area= (baseM + basem)/2 * altura
    return area

#Recibe base mayor, menor y altura y regresa perimetro
def calcularPerimetro(baseM, basem, altura):
    lado= (((baseM - basem)/2)**2 + (altura)**2)**.5
    perimetro= basem + baseM + (lado*2)
    return perimetro

#Recibe area y perimetro y lo imprime
def imprimir (area, perimetro):
    print("Area: %.2f"% area)
    print("Perimetro: %.2f"% perimetro)

#Principal, resuelve el problema
def main():
    baseM= int(input("Teclea la base Mayor :"))
    basem= int(input("Teclea la base menor :"))
    altura= int(input("Teclea la altura :"))
    area= calcularArea(baseM, basem, altura)
    perimetro= calcularPerimetro(baseM, basem, altura)
    imprimir(area, perimetro)


#Llama a la función main
main()