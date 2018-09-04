#Autor: Patricio Mondragón
#Este programa calcula el area y perimetro de un trapecio con funciones.
import math

def calcularareadeltrapecio(basegrande,basepequeña,alturadeltriangulo):
    areadeltrapecio= ((basegrande+basepequeña)/2)*alturadeltriangulo
    return areadeltrapecio


def calcularelperimetrodeltrapecio(alturadeltriangulo,basepequeña,basegrande):
    hipotenusa= alturadeltriangulo/math.sin(65)
    perimetrodeltriangulo= (hipotenusa*2)+basepequeña+basegrande

    return perimetrodeltriangulo





def main():
    basegrande= int(input("Teclea el valor de la base grande:"))
    basepequeña= int(input("Teclea el valor de la base pequeña:"))
    alturadeltriangulo= int(input("teclea la altura dl triangulo:"))
    areadeltrapecio=calcularareadeltrapecio(basegrande,basepequeña,alturadeltriangulo )
    perimetrodeltriangulo= calcularelperimetrodeltrapecio(alturadeltriangulo,basepequeña,basegrande)
    print("El area del trapecio es:%.2f"%(areadeltrapecio))
    print("El perimetro del trapecio es:%.2f"%(perimetrodeltriangulo))

main()
