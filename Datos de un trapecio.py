#Autor;Diana Marisol Medina Bravo
#Lee la base menor, la base mayor y la altura de un trapecio isósceles y se imprime el área y el perímetro


#Función para calcular el área del trapecio
#Recibe el valor de la base mayor, la base manor y la altura y regresa el área
def calcularArea (baseMayor,baseMenor,altura):
    area= ((baseMayor+baseMenor)/2)*altura
    return area

#Función para calcular el perímetro del trapecio
#Recibe el valor de la base mayor, la base manor y la altura y regresa el perímetro
def calcularPerimetro (baseMayor,baseMenor,altura):
   cateto=(baseMayor-baseMenor)/2
   hipotenusa=((cateto**2)+(altura**2))**.5
   perimetro=(hipotenusa*2)+baseMenor+baseMayor
   return perimetro

#Función principal, resuelve el problema
def main():
    baseMayor= int(input("Escribe la longitud de la base mayor: "))
    baseMenor= int(input("Escribe la longitud de la base menor: "))
    altura= int(input("Escribe la altura: "))
    area= calcularArea(baseMayor,baseMenor,altura)
    perimetro= calcularPerimetro(baseMayor,baseMenor,altura)
    print("Área: %.2f" % area)
    print("Perímetro: %.2f" % perimetro)

#Llamar a la función
main()
