#Nombre: Saúl Figueroa Conde.
#Matrícula: A01747306.
#Programa: Este programa lee la base mayor, la base menor y la altura de un trapecio isósceles para imprimir
#el valor de su área y perímetro.

#Se importa la biblioteca math para realizar operaciones que requieran sacar raíz cuadrada.
import math


#Se define la función que calcurará el área del trapecio isósceles (calcularÁrea). La función recibe como parámetros el valor de
#la base mayor, base menor y altura del trapecio. Al final, la función regresa el valor del área.
def calcularÁrea(B, b, h):
    área = (B + b) / 2 * (h)
    return área

#Se define la función que calcurará el perímetro del trapecio isósceles (calcularPerímetro). La función recibe como parámetros el valor de
#la base mayor, base menor y altura del trapecio. Al final, la función regresa el valor del perímetro.
def calcularPerímetro(B, b, h):
    perímetro = ((B - b) / 2)
    perímetro = (perímetro ** 2) + (h ** 2)
    perímetro = math.sqrt(perímetro)
    perímetro = B + b + 2 * perímetro
    return perímetro

#Ésta es la función main. El usuario indica el valor de la base mayor, base menor y altura del trapecio isósceles.
#Los valores indicados se envían a las funciones de calcularÁrea y calcularPerímetro para que regrese el valor del área
#y el perímetro del trapecio. Por último, imprime el resultado del área y el perímetro con 2 decimales de precisión.
def main():
    baseMayor = float(input("Escribe la longitud de la base mayor: "))
    baseMenor = float(input("Escribe la longitud de la base menor: "))
    altura = float(input("Escribe la altura: "))

    área = calcularÁrea(baseMayor, baseMenor, altura)
    perímetro = calcularPerímetro(baseMayor, baseMenor, altura)

    print("Área: %.2f" % (área))
    print("Perímetro: %.2f" % (perímetro))

#El programa llama aquí a la función main para resolver el problema en cuestión, calculando el valor del área y el
#perímetro del trapecio isósceles.
main()
