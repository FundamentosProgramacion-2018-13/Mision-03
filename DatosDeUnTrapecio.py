#Autor: Jesus Zabdiel Sanchez Chavez A01374964

#Descripcion: calcula el area y el perimetro de un traingulo isosceles con base e una base menor, base mayor y altura.


#funcion principal
def main ():
    bmayor = int(input("Inserta el valor de la base mayor: "))
    bmenor = int (input("Inserta el valor de la base menor: "))
    altura = int (input("inserta el valor de la altura: "))
    area = calcularArea(altura, bmayor, bmenor)
    perimetro = calcularPerimetro(altura, bmenor,bmayor)
    print ("Área: %.2f" % area)
    print ("Perímetro: %.2f " %perimetro)


#Calcula el area del trapecio
def calcularArea (altura, bmenor, bmayor):
    area = altura * ((bmenor)+(bmayor))/ 2
    return area
#calcula un lado del trapecio y el perimetro completo
def calcularPerimetro(altura, bmenor, bmayor):
    basetri= (bmayor-bmenor)/2
    lado = (((basetri**2) + (altura**2)))**.5
    perimetro = bmayor + bmenor + 2*lado
    return perimetro

main()