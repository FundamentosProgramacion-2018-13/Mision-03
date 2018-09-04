# Autor: Ithan Alexis Pérez Sánchez
# Saber Área y Perímetro de un trapecio


# La linea de codigo empieza después de esta linea

def Calcular_Triangulo(Base_Mayor, Base_Menor, Altura): # Ayuda de formula para poder determinar los lados del trapecio
    Lado_A = (Base_Mayor - Base_Menor) / 2
    Lado_B = Altura
    Lado_C = (Lado_A **2 + Lado_B **2 )** 0.5
    C = Lado_C
    return C

def Calcular_Perimetro(Base_Mayor, Base_Menor, Altura):     # Formula para sacar Perímetro
    Perímetro = Base_Mayor + Base_Menor + Calcular_Triangulo(Base_Mayor, Base_Menor, Altura) * 2
    return Perímetro

def Calcular_Area(Base_Mayor, Base_Menor, Altura):      # Formula para sacar Área
    Área = ((Base_Mayor + Base_Menor) * Altura) / 2
    return Área

def Imprimir(Base_Mayor, Base_Menor, Altura):   # Se imprime el Área y el Perímetro de nuestra figura
    print("Área es = %.2f" % (Calcular_Area(Base_Mayor, Base_Menor, Altura)))
    print("Perímetro es = %.2f" % (Calcular_Perimetro(Base_Mayor, Base_Menor, Altura)))

def main():                    # Nuestra principal función para ingresar datos y determinar el calculo
    Base_Mayor = int(input("La Longitud de la base mayor: "))
    Base_Menor = int(input("La Longitud de la base menor: "))
    Altura = int(input("La Altura: "))
    Imprimir(Base_Mayor, Base_Menor, Altura)

main()
