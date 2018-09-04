# Autor: Oscar Alejandro Torres Maya, A01377686, grupo 04
# Descripción: Programa que calcula el rendimiento de un auto en kilometros sobre litro y millas sobre galones
# Además de calcular cuánta gasolina necesita para determinados kilometros

#Valores que no cambian
milla = 1.6093 #km
galon = 0.264 #1 litro

# Función para calcular kilometros sobre litros
def kilometrosSobreLitros (kilometrosRecorridos, litrosUsados):
    kilometrosLitro = kilometrosRecorridos/litrosUsados
    return kilometrosLitro

# Función para calcular millas sobre galones
def millasSobreGalones (kilometrosRecorridos, litrosUsados):
    millasGalon = (kilometrosRecorridos/milla)/(litrosUsados*galon)
    return millasGalon

# Función para calcular gasolina necesaria para aguantar determinados kilometros
def gasolinaTraslado (kilometrosRecorrer, litrosUsados, kilometrosRecorridos):
    gasolinaNecesaria = (kilometrosRecorrer*litrosUsados)/kilometrosRecorridos
    return gasolinaNecesaria

# Función principal, lee datos e imprime datos. Además de poner texto en negrita.
def main():
    kilometrosRecorridos = int(input("Teclea el número de km recorridos: "))
    litrosUsados = int(input("Teclea el número de litros de gasolina usados: "))
    kilometroslitro = kilometrosSobreLitros (kilometrosRecorridos, litrosUsados)
    millasGalon = millasSobreGalones (kilometrosRecorridos, litrosUsados)

    print("")
    print("\033[1;30m"+"Si recorres", kilometrosRecorridos, "\033[1;30m"+ "kms con ", litrosUsados,"\033[1;30m"+ "litros de gasolina, el rendimiento es: ")
    print("%0.2f" % (kilometroslitro), " km/l")
    print("%0.2f" % (millasGalon), " mi/gal")

    print("")
    kilometrosRecorrer= int(input("\033[0;30m"+"¿Cuántos kilómetros vas a recorrer? "))
    gasolinaNecesaria= gasolinaTraslado (kilometrosRecorrer, litrosUsados, kilometrosRecorridos)
    print("")
    print("\033[1;30m"+"Para recorrer", kilometrosRecorrer, "\033[1;30m"+"km. necesitas %0.2f" % (gasolinaNecesaria), "\033[1;30m"+"litros de gasolina")

main()