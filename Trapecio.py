# Autor: Francisco Ariel Arenas Enciso
# Actividad : Cálculo del área y perímetro de un trapecio


'''
Esta función es la responsable de recibir los datos de entrada (medidas de la base menor, mayor y altura) de la función
main, los almacena en variables y con dichas variables hace las operaciones artimeticas necesarias para devolver el
valor del área.
'''

def calcularArea(baseMayor, baseMenor, altura):
    area = ((baseMayor+baseMenor)/2) * altura
    return area


'''
Esta función es la responsable de recibir los datos de entrada (medidas de la base menor, mayor y altura) de la función
main, los almacena en variables y con dichas variables hace las operaciones artimeticas necesarias para devolver el 
valor del perimetro.
'''

def calcularPerimetro(baseMayor, baseMenor, altura):
    baseTriangulorectangulo = (baseMayor-baseMenor)/2
    hipotenusa = ((altura**2)+(baseTriangulorectangulo**2))**0.5
    perimetro = baseMayor + baseMenor + (2*hipotenusa)
    return perimetro


'''
Función main (Es la responsable del funcionamiento de todo el programa).
Primero le pide al usuario las medidas de cada uno de los lados del trabecio (base menor, mayor, y la altura).
Envía estos datos a las funciónes 'área' y 'perimetro' respectivamente para que éstas puedan trabajar 
Finalmente imprime el área y perimetro del trapecio.  
'''

def main ():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud la base menor: "))
    altura = int(input("Escribe la altura: "))
    area = (calcularArea(baseMayor, baseMenor, altura))
    perimetro = (calcularPerimetro(baseMayor, baseMenor, altura))
    print("El área del trapecio es: %5.2f m" % (area))
    print("El permitero del trapecio es: %5.2f m" % (perimetro))


main()



