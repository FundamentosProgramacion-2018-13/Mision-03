#Autor: Alan Diaz Carrera
#Descripción: Calcular area y perimetro de un trapecio isoceles

baseMay=int(input("Escribe la lomgitud de la base mayor:"))
baseMen=int(input("Escribe la longitud de la base menor:"))
altura=int(input("Escribe la altura:"))

#Calcula el perimetro
def perimetroTra():
    perimetro=baseMen+baseMay+ 2*(((altura)**2+(baseMen/2)**2)**0.5)
    print("Perimetro: %.2f"%(perimetro))

#Calcula el area
def areaTra():
    area = ((baseMay+baseMen)/2)*altura
    print("Area: %.2f"%(area))

def main():
    perimetroTra()
    areaTra()

main()