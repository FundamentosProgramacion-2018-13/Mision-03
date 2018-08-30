#Jesús Roberto Herrera Vieyra // A01377230
#Programa para calcular el rendimiento de un auto

#función para calcular el rendimiento del coche
def calcularrendimiento(kilometros,litros):
    rendimiento= kilometros/litros

    return rendimiento

#función para convertir a millas/galones
def convertirUnidades(kilometros,litros):

    millas = kilometros/1.6093
    galones = litros*0.264
    rendimiento = millas/galones

    return rendimiento

#Procedimiento principal
def main():

    kilometros= int(input("Teclea el número de km recorridos: "))
    litros= int(input("Teclea el número de litros de gasolina usados: "))

    rendimiento = calcularrendimiento(kilometros,litros)
    conversion = convertirUnidades(kilometros,litros)

    print("Si recorres %d km con %d litros de gasolina, el rendimiento es: " %(kilometros,litros))
    print("{0:.2f}".format(rendimiento),"km/l")
    print("{0:.2f}".format(conversion),"mi/gal")


    distancia = int(input("¿Cuántos kilómetros vas a recorrer? "))
    litrosNecesarios = distancia/rendimiento

    print("Para recorrer ",distancia," km. Necesitas ","{0:.2f}".format(litrosNecesarios)," litros de gasolina")





main()
