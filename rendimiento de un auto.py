# Autor: Rubén Villalpando Bremont
# El programa calcula el rendimiento de tu auto en km/l y mi/gal y después te dice la cantidad de litros necesarios para recorrer cierta cantidad de km.


# Calcula el número de litros necesarios para recorrer cierta distancia en km
def litrosParaRecorrerKm(kilometrosPorRecorrer, kilometrosPorLitro):
    litrosNecesariosParaRecorrer = kilometrosPorRecorrer/kilometrosPorLitro
    return litrosNecesariosParaRecorrer


# Calcula el rendimiento de el coche en millas por galón
def miPorGalon(kilometros, litros):
    millas = kilometrosAMillas(kilometros)
    galones = litrosAGalon(litros)
    rendimientoEnGalones = millas/galones
    return rendimientoEnGalones

# Convierte los litros a galones
def litrosAGalon(litros):
    galones = litros*0.264
    return galones

# Convierte los kilómetros a millas
def kilometrosAMillas(kilometros):
    millas = kilometros*0.621
    return millas

# Calcula el rendimiento de el coche en kilómetros por litro
def kmPorLitro(kilometros, litros):
    rendimiento = kilometros/litros
    return rendimiento

# Función main
def main():
    kilometrosRecorridos = int(input("Teclea el número de km recorridos: "))
    gasolinaUtilizada = int(input("Teclea el número de litros de gasolina usados: "))
    kilometrosPorLitro = kmPorLitro(kilometrosRecorridos, gasolinaUtilizada)
    millasPorGalon = miPorGalon(kilometrosRecorridos, gasolinaUtilizada)
    print("Si recorres %.0d kms con %.0f litros de gasolina, el rendimiento es:" % (kilometrosRecorridos, gasolinaUtilizada))
    print("%.2f km/gal" % (kilometrosPorLitro))
    print("%.2f mi/gal" % (millasPorGalon))
    kmsPorRecorrer = int(input("¿Cuántos kilómetros vas a recorrer? "))
    litrosNecesarios = litrosParaRecorrerKm(kmsPorRecorrer, kilometrosPorLitro)
    print("Para recorrer %0.d km. necesitas %.2f litros de gasolina" % (kmsPorRecorrer, litrosNecesarios))

# Llamar a main
main()
