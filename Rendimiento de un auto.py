# Oscar Macias Rodríguez
# Descripción: Calcula el rendimiento de un automóvil (km/litro, millas/gal.).
# Indica la cantidad de litros que necesitará para viajar cierta cantidad de km.

# Convierte km/litro a millas/galón
def convertirMillasPorGalon(km, litros):
    kmLitro = km / litros
    miGalon = kmLitro * 2.35397
    return miGalon

# Calcula la cantidad de litros que se necesitan para recorrer cierta cantidad de kilómetros
def calcularLitros(km1):
    k = 27.93
    litro = km1/k
    return litro

# Imprime en pantalla km/litros, mi/gal y la cantidad de litros requeridos para recorrer cierta cantidad de kms.
def main():
    km = int(input("Teclea el número de km recorridos:"))
    litros = int(input("Teclea el número de litros de gasolina usados:"))
    kmLitro = km / litros

    miGal = convertirMillasPorGalon(km, litros)
    print()
    print("Si recorres", km, "kms con", litros, "litros de gasolina, el rendimiento es:")
    print("%.2f" % kmLitro, "km/l")
    print("%.2f" % miGal, "mi/gal")
    print()

    km1 = int(input("¿Cuántos kilómetros vas a recorrer?"))
    litro = calcularLitros(km1)
    print()
    print("Para recorrer", km1, "km. necesitas", "%.2f" % litro, "litros de gasolina")

main()