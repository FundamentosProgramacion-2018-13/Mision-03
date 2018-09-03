# JavierAlexandro Vargas Sánchez A01377718
'''Programa que calcula el rendimiento de la gasolina y predice la cantidad necesaria de gasolina
para recorrer un número de kilómetros introducidos por el usuario'''


def calculaRendimientoEnKmL(kmRecorridos, litrosUsados):  #Calcula el rendimiento en la relacion kilometros y litros
    rendimientokml = kmRecorridos / litrosUsados
    return rendimientokml


def calculaRendimientoEnMilG(kmRecorridos, litrosUsados): #Convierte de kilometros y litros a millas y galones, igual calcula el rendimiento en la relación
    millas = kmRecorridos * 0.62138818119679
    galones = litrosUsados * 0.264
    rendimientomigal = millas / galones
    return rendimientomigal


def imprimir1(kmRecorridos, litrosUsados, rendimientokml, rendimientomigal):  #Imprime el rendimeinto en los tipos de unidades
    print()
    print("Si recorres", kmRecorridos, "kms con",litrosUsados,"litros de gasolina el rendimiento es:" )
    print(format(rendimientokml, ".2f"),"km/l")
    print(format(rendimientomigal, ".2f"),"mi/gal")
    print()


def calcularGasNecesaria(kmCaso, kmRecorridos, litrosUsados):  # Calcula la gasolina necesaria para recorrer un número de kimlómetros determinado por el usuario
    gasNecesaria = (kmCaso * litrosUsados) / kmRecorridos
    return gasNecesaria


def imprimir2(kmCaso, gasNecesaria): #Imprime el la gasolina necesaria para recorrer cierto número de kilómetros, basado en el renidmiento de auto
    print()
    print("Para recorrer", kmCaso,"km. necesitas",format(gasNecesaria, ".2f"), "litros de gasolina")


def main():
    kmRecorridos = int(input("Teclea el número de km recorridos: "))
    litrosUsados = int(input("Teclea el número de litros de gasolina usados: "))
    rendimientokml = calculaRendimientoEnKmL (kmRecorridos, litrosUsados)
    rendimientomigal = calculaRendimientoEnMilG (kmRecorridos, litrosUsados)
    imprimir1 (kmRecorridos, litrosUsados,rendimientokml, rendimientomigal)
    kmCaso = int(input("¿Cuántos kilómetros vas a recorrer?: "))
    gasNecesaria = calcularGasNecesaria (kmCaso, kmRecorridos, litrosUsados)
    imprimir2 (kmCaso, gasNecesaria)

main()