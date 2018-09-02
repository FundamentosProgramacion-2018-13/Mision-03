#Autor;Diana Marisol Medina Bravo
'''
Lee el número de kilómetros recorridos, la cantidad de gasolina en litros e imprime el rendimiento en
kilómetros/litros y en millas/galones.
Después lee cuantos kilómetros se van a recorrer y se cálcula e imprime los litros de gasolina necesarios para recorrer
esos kilómetros.
'''


#Función para calcular el rendimiento en km/litros
#Recibe el número de km recorridos y la cantidad de gasolina y regresa el rendimiento en km
def calcularRendimientoKmLitros(numeroDeKmRecorridos,cantidadDeGasolinaLitros):
    rendimientoAutoKmLitros=numeroDeKmRecorridos/cantidadDeGasolinaLitros
    return rendimientoAutoKmLitros

#Función para calcular el rendimiento en millas/galones
#Recibe el número de km recorridos y la cantidad de gasolina en litros, se hace una conversión y regresa el rendimiento en millas/galones
def calcularRendimientoMillasGalones(numeroDeKmRecorridos,cantidadDeGasolinaLitros):
    rendimientoAutoMillasGalon=numeroDeKmRecorridos/(cantidadDeGasolinaLitros*1.6093*0.264)
    return rendimientoAutoMillasGalon

#Función para calcular la gasolina necesaria en litros para recorrer cierta distancia en km
#Recibe los km que se van a recorrer o viajar y el rendimiento del auto en km/litros y regresa la gasolina necesaria en litros
def calcularGasolinaNecesariaEnLitros(kmAViajar, rendimientoAutoKmLitros):
    gasolinaNecesariaEnLitros=kmAViajar/rendimientoAutoKmLitros
    return gasolinaNecesariaEnLitros

#Función principal, resuelve el problema
def main():
    numeroDeKmRecorridos=int(input("Teclea el número de km recorridos: "))
    cantidadDeGasolinaLitros= int(input("Teclea el número de litros de gasolina usados: "))
    rendimientoAutoKmLitros=calcularRendimientoKmLitros(numeroDeKmRecorridos,cantidadDeGasolinaLitros)
    rendimientoAutoMillasGalon=calcularRendimientoMillasGalones(numeroDeKmRecorridos,cantidadDeGasolinaLitros)
    print("")
    print(chr(27) + "[1;30m" + "Si recorres", numeroDeKmRecorridos, "kms con", cantidadDeGasolinaLitros,
          "litros de gasolina, el rendimiento es:")
    print("%.2f" % rendimientoAutoKmLitros, "km/l")
    print("%.2f" % rendimientoAutoMillasGalon, "mi/gal")
    print(chr(27) + "[0;30m" + "")
    kmAViajar=int(input("¿Cuántos kilómetros vas a recorrer? "))
    gasolinaNecesariaEnLitros= calcularGasolinaNecesariaEnLitros(kmAViajar,rendimientoAutoKmLitros)
    print("")
    print(chr(27) + "[1;30m" + "Para recorrer", kmAViajar, "km. necesitas %.2f" % gasolinaNecesariaEnLitros,
          "litros de gasolina")


#Llama a la función
main()