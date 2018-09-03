# Autor: Jonathan Sanabria Rocha
# Calcular el rendimiento de un auto

import math

def calcularRendimientokmL(kmrecorridos,litrosgas):
    rendimientokml = kmrecorridos / litrosgas
    return rendimientokml
#Calcula el rendimiento en km/l de los valores dados por el usuario.

def calcularRendimientomigal(rendimientokml):
    milla = 1.6093
    litro = 0.264
    rendimientomigal = rendimientokml / milla / litro
    return rendimientomigal
#Hace la conversion de unidades del rendimiento del carro.

def calcularLitrosnecesarios (kmarecorrer,rendimientokml):
    linecesarios = rendimientokml/kmarecorrer
    return linecesarios
#Caalcula los litros necesarios para recorrer los km dados por el usuario.

def main():
    kmrecorridos = int(input("Teclea el numero de km recorridos: "))
    litrosgas = int(input("Teclea el numero de litros de gasolina usados: "))
    rendimientokml = calcularRendimientokmL(kmrecorridos,litrosgas)
    rendimientomigal = calcularRendimientomigal(rendimientokml)
    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es: " % (kmrecorridos,litrosgas))
    print(" % .2f km/l" % rendimientokml)
    print(" % .2f mi/gal" % rendimientomigal)

    kmarecorrer = int(input("¿Cuantos kilometros vas a recorrer? "))
    linecesarios = calcularLitrosnecesarios(rendimientokml,kmarecorrer)

    print("Para recorrer %.0f km. necesitas %.2f litros de gasolina" % (kmarecorrer,linecesarios))

main()
