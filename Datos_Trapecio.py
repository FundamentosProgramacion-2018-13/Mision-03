#Autor: Luis Mario Cervantes Ortiz
#Calcular el área y perímetro de un trapecio pidiendo: Base mayor, base menor y altura

def calcularArea(baseM,basem,altura): #Calcular el area
    calcularArea=((baseM+basem)/2)*altura
    return calcularArea
def calcularPerimetro(baseM,basem,altura): #Calcular el perímetro, hipotenusa y lado
    lado= (baseM-basem)/2
    hipotenusa=(lado**2+altura**2)**(1/2)
    calcularPerimetro=(baseM+basem++hipotenusa*2)
    return calcularPerimetro

def main(): #Preguntar datos
    baseM=int(input("Escribe la longitud de la base mayor:"))
    basem = int(input("Escribe la longitud de la base menor:"))
    altura=int(input("Escribe la altura:"))
#Summonear funciones
    totalArea=calcularArea(baseM,basem,altura)
    totalPerimetro=calcularPerimetro(baseM,basem,altura)

    print("Área: %.2f"%(totalArea))
    print("Perímetro: %.2f"%(totalPerimetro))

main()