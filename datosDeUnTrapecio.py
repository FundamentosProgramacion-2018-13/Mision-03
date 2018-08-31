#Autor: Marco González Elizalde
'''Proposito: Calcular e imprimir el area y perimetro de un trapecio isósceles
preguntando al usuario los valores de la base mayor, base menor y altura'''

#Calcula el area del trapecio isoceles, regresa valor del area
def calcularArea(baseMayor,baseMenor,altura):
    area = (baseMayor + baseMenor) /2 *altura
    return area

#Calcula el valor de un lado del trapecio y del perimetro, regresa valor del perímetro
def calcularPerimetro(baseMayor,baseMenor,altura):
    # Calcula el lado del trapecio utilizando el teorema de pitagoras
    lado = ((altura **2) + (((baseMayor - baseMenor)/2) **2)) **0.5
    
    perimetro = baseMayor + baseMenor + (lado *2)
    return perimetro

'''Pregunta al usuario los valores de las bases y altura del trapecio,
calcula y despues imprime el valor del área y del perímetro'''
def main():
    baseMayor = float(input("Escribe la longitud de la base mayor: "))
    baseMenor = float(input("Escribe la longitud de la base mmenor: "))
    altura = float(input("Escribe la altura: "))

    area = calcularArea(baseMayor,baseMenor,altura)
    perimetro = calcularPerimetro(baseMayor,baseMenor,altura)

    print("""Área: %.02f
Perímetro: %.02f""" %(area, perimetro))

#Corre el programa
main()
