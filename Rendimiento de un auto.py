# Autor: Humberto Carrillo Gómez
"""Descripción: Este programa calcula el rendimiento de un automóvil en kilometros/litro y millas/galón e imprime los
litros de gasolina que necesitará para recorrer cierto kilometraje"}"""

#Calcula el rendimiento en km por litro utlizando los km recorridos y los litros de gasolina utilizados
def calcularRendimientoKm(km, litrosGas):
    rendimientoKm= km/litrosGas
    return rendimientoKm
# Convierte los km recorridos a millas
def calcularMillas(km):
    millas= km/1.6093
    return millas

# Convierte los litros de gasolina a galones
def calcularGalones(litrosGas):
    galones= litrosGas*0.264
    return galones
# Calcula el rendimiento en millas por galón utilizando las millas recorridas y los galones de gasolina utilizados.
def calcularRendimientoMillas(millas, galones):
    millasPorGalon= millas/galones
    return millasPorGalon

# Calcula los litros de gasolina que serán necesarios para recorrer cierta distancia
def calcularGas(km,litrosGas,kmPorRecorrer):
    gasolinaNecesaria= (kmPorRecorrer*litrosGas)/km
    return gasolinaNecesaria


# Función principal, incorpora a las funciones anteriormente creadas para resolver el problema e impreme las salidas.
def main():
    km= int(input("Teclea el número de kilometros recorridos: "))
    litrosGas= int(input("Teclea el número de litros de gasolina usados: "))
    rendimientoKm= calcularRendimientoKm(km,litrosGas)
    millas=calcularMillas(km)
    galones=calcularGalones(litrosGas)
    rendimientoMillasPorGalon= calcularRendimientoMillas(millas,galones)
    print()
    print("Si recorres",km,"km con",litrosGas,"litros, el rendimiento es:")
    print(format(rendimientoKm,".2f"), "km/l")
    print(format(rendimientoMillasPorGalon,".2f"), "mi/gal")
    print()
    kmPorRecorrer = int(input("¿Cuántos kilometros vas a recorrer? "))
    gasolinaNecesaria = calcularGas(km, litrosGas, kmPorRecorrer)
    print()
    print("Para recorrer",kmPorRecorrer,"necesitas",format(gasolinaNecesaria,".2f"),"litros de gasolina")

# Llamar a la función principal
main()