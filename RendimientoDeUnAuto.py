# Autor: Luis Humberto Burgueño Paz
# Calcula el rendimiento de la gasolina y dice al usuario la cantidad de litros necesitados para cierta cantidad de kilómetros

# Recibe como parámetros los kilometros recorridos y los litros gastados y regresa los kilómetros recorridos por litro
def calcularKmL(kilometros, litros):
    kmL = kilometros / litros
    return kmL

#Recibe como parámetros los kilómetros recorridos y los litros gastados y regresa las millas recorridas por galón
def calcularMiG(kmL):
    miGal = kmL / (1.6093 * 0.264)
    return miGal

# Recibe como parámetros los kilómetros por recorrer y regresa los litros necesitados de gasolina
def calcularLitros(kilometrosPorRecorrer, kmL):
    litrosNecesitados = kilometrosPorRecorrer / kmL
    return litrosNecesitados
# Lee los km y los litros e imprime los km/l y mi/gal
def main():
    kilometros = int(input("Teclea el número de km recorridos: "))
    litros = int(input("Teclea el número de litros de gasolina usados: "))
    kmL = calcularKmL(kilometros, litros)
    miGal = calcularMiG(kmL)
    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es:" % (kilometros, litros))
    print("%.02f km/l" % kmL)
    print("%.02f mi/gal" % miGal)
    kilometrosPorRecorrer = int(input("¿Cuántos kilómetros vas a recorrer? "))
    litrosNecesitados = calcularLitros(kilometrosPorRecorrer, kmL)
    print("Para recorrer %d km. necesitas %.02f litros de gasolina" % (kilometrosPorRecorrer, litrosNecesitados))
main()
