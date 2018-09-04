#Rodolfo Anibal Altamirano Sánchez, A01377949
#Se necesita calcular los litros que un vehículo utiliza por kilometro, asi como las millas por galon. Después ver cunatos litros necesitaria para recorrer cierta distancia.


#Cálcula los litros por kilometro utilizados
def calcularKmPorLitro(kilometrosRecorridos, litrosUsados):
    kmPorLitro = kilometrosRecorridos/litrosUsados
    return kmPorLitro

#Convierte los litros gastados a galones
def convertirLitroasGalones(litrosUsados):
    galUsados =  litrosUsados*0.264
    return galUsados

#Convierte los kilometros recorridos a millas
def convertirMillasKilometros(kilometrosRecorridos):
    miUsadas = kilometrosRecorridos / 1.6093
    return miUsadas


# Hace la regla de 3 para ver las millas por galon
def calcularMiPorGalon(kilometrosRecorridos, litrosUsados):
     galUsados = convertirLitroasGalones(litrosUsados)
     miUsadas = convertirMillasKilometros(kilometrosRecorridos)
     miPorGalon = miUsadas/galUsados
     return miPorGalon

#cCálcula los litros necesarios para recorrer la distancia que se nos da
def calcularLitrosNcesarios(kilometrosRecorridos, litrosUsados, kmPorRecorrer):
    kmPorLitro = calcularKmPorLitro(kilometrosRecorridos, litrosUsados)
    litrosNecesarios = kmPorRecorrer/kmPorLitro
    return litrosNecesarios



#Llama todas las funciones
def main():
    #Pide los datos principales (km recorridos y litros usados)
    kilometrosRecorridos = float(input("Teclea el número de  km recorridos: "))
    litrosUsados = float(input("Teclea el número de litros usados: "))

    kmPorLitro = calcularKmPorLitro(kilometrosRecorridos, litrosUsados)
    miPorGal = calcularMiPorGalon(kilometrosRecorridos, litrosUsados)


    #imprime los resultados con texto
    print("Si recorres", kilometrosRecorridos, "kms con", litrosUsados ,"litros de gasolina, el rendimiento es:")
    print("%.2f" % kmPorLitro,"km/l")
    print("%.2f" % miPorGal,"mi/gal")


    #Pide los kilometrros que se quieren recorrer
    kmPorRecorrer = float(input("¿Cuántos kilómetros vas a recorrer? "))
    litrosNecesarios = calcularLitrosNcesarios(kilometrosRecorridos, litrosUsados, kmPorRecorrer)
    #imprime los litros necesaris
    print("Para recorrer", kmPorRecorrer," km. necesitas %.2f" % litrosNecesarios,"litros de gasolina")



main()