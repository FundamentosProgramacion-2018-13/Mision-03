#Joshua Sánchez Martínez A01274269
#Pedide los kilometros y litros de su auto para calcular el rendimiento
#además de proporcionar una cantidad necesaria para una distancia

def calcularRendimientoEnKm(kmR,lU):

    rendimiento = kmR/lU

    return rendimiento


def conversionMillas(kmR,lU):

    conversion = (kmR/1.6093)/(lU*0.264)

    return conversion

def litrosParaRecorrer(rendimiento, distancia):

    litrosAUsar = distancia/rendimiento

    return litrosAUsar

def main():

    kmRecorridos = int(input("Teclea el numero de km recorridos: "))
    lUsados = int(input("Teclea el numero de litros de gasonlina usados: "))

    rendimientoKm = calcularRendimientoEnKm(kmRecorridos, lUsados)
    conversion = conversionMillas(kmRecorridos, lUsados)

    print("si recorres", kmRecorridos, "kms con", lUsados, "el redimiento es: ")
    print("%.2f" % rendimientoKm, "km/l")
    print("%.2f" % conversion, "mi/gal")

    kmPorRecorrer = int(input("¿Cuantos km vas a recorrer? "))

    #Ya que se necesita el resultado de una función, esta se introduce acontinuación

    litrosNecesarios = litrosParaRecorrer(calcularRendimientoEnKm(kmRecorridos,lUsados),kmPorRecorrer)

    print("Para recorrer", kmPorRecorrer, "necesitas %.2f" % litrosNecesarios, "litros de gasolina")




main()