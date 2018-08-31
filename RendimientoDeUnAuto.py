# Autor: Erick David Ramírez Martínez, A01748155, Grupo: 2
""" Descripción: Programa para calcular el rendimiento de un auto en km/litro y millas/galon e imprima el posible consumo de combustible
de acuerdo a los kilómetros que recorrerá en el futuro """

def calculoDeRendimiento(kilometros,litros):
    rendimientoKML = kilometros/litros

    return rendimientoKML


def conversionDeRendimiento(kilometros,litros):
    rendimientoMiGal = (kilometros/1.6093)/(litros*0.264)

    return rendimientoMiGal


def litrosAUtilizar(rendimientoKML,distanciaFutura):
    litrosNecesarios = distanciaFutura/rendimientoKML

    return litrosNecesarios


def main():
    kilometros = float(input("Ingrese los kilómetros recorridos: "))
    litros = float(input("Ingrese los litros de gasolina consumidos: "))

    rendimientoKML = calculoDeRendimiento(kilometros,litros)
    rendimientoMiGal = conversionDeRendimiento(kilometros,litros)

    print("")
    print("El automovil recorre %0.2f km usando %0.2f litros de gasolina, entonces el rendimiento es: " % (kilometros,litros))
    print("%0.2f km/l" %(rendimientoKML))
    print("%0.2f mi/gal" %(rendimientoMiGal))
    print("")

    distanciaFutura = float(input("Ingrese los kilómetros que recorrerá: "))
    print("")

    litrosNecesarios = litrosAUtilizar(rendimientoKML,distanciaFutura)

    print("Para recorrer %0.2f km, se necesitan %0.2f litros de gasolina" %(distanciaFutura,litrosNecesarios))


main()