# Autor: Marco González Elizalde
'''Proposito: Calcular el rendimiento de un auto en Km/L y en Mi/Gal
y dar la cantidad de gasolina necesaria para un viaje de ciertos Km'''


# Calcula el rendimiento del coche en Km/L
def calcularRendimientoKm(kmRecorridos, litrosUsados):
    rendimientoEnKm = kmRecorridos / litrosUsados
    return rendimientoEnKm


# Convierte el valor del rendimiento en Km/L a Mi/Gal
def convertirAMillasPorGalon(rendimientoEnKm):
    rendimientoEnMi = rendimientoEnKm / 1.6093 / 0.264
    return rendimientoEnMi


# Calcula la cantidad de gasolina necesaria para realizar un viaje de ciertos Km
def calcularGasNecesaria(kmDeViaje, rendimientoEnKm):
    gasNecesaria = kmDeViaje / rendimientoEnKm
    return gasNecesaria


'''Pregunta por los km recorridos por el usuario, la gasolina utilizada
y la extension del viaje, regresa el rendimiento en Km/L y Mi/Gal, y
la gasolina necesaria para el viaje'''


def main():
    kmRecorridos = float(input("Teclea el número de km recorridos: "))
    litrosUsados = float(input("Teclea el número de litros de gasolina usados: "))
    print("")

    rendimientoEnKm = calcularRendimientoKm(kmRecorridos, litrosUsados)
    rendimientoEnMi = convertirAMillasPorGalon(rendimientoEnKm)

    print("""Si recorres 475 kms con 17 litros de gasolina, el rendimiento es:
%.02f km/l
%.02f mi/gal
""" % (rendimientoEnKm, rendimientoEnMi))

    kmDeViaje = int(input("¿Cuántos kilómetros vas a recorrer? "))
    print("")
    gasRequerida = calcularGasNecesaria(kmDeViaje, rendimientoEnKm)

    print("Para recorrer %d km. necesitas %.02f litros de gasolina"
          % (kmDeViaje, gasRequerida))


# Ejecuta el programa
main()
