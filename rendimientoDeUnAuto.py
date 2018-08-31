#Autor: Alejandro Torices Oliva
#Es un programa que calcula el rendimiento de un automovil y la gasolina necesaria para cierto recorrido.

#Calcula el rendimiento del vehiculo al dividir los kilometros recorridos entre
#la cantidad de gasolina utilizada.
def calcularRendimiento(kmRecorridos, litrosDeGasolina):
    rendimiento = kmRecorridos / litrosDeGasolina
    return rendimiento

#Calcula la equivalencia del rendimiento del vehículo en millas por galón.
def calcularEquivalencia(rendimiento):
    equivalencia = rendimiento / 1.6093 / 0.264
    return equivalencia

#Calcula la cantidad de gasolina necesaria para realizar cierto recorrido.
def calcularGasolina(kilometrosPorRecorrer, rendimiento):
    gasolinaNecesaria = kilometrosPorRecorrer / rendimiento
    return gasolinaNecesaria

#Es la función principal, obtiene los datos e imprime las soluciones.
def main():
    kmRecorridos = int(input("Teclea el número de km recorridos: "))
    litrosDeGasolina = int(input("Teclea el número de litros de gasolina usados: "))
    rendimiento = calcularRendimiento(kmRecorridos, litrosDeGasolina)
    equivalencia = calcularEquivalencia(rendimiento)
    print("""
Si recorres %d kms con %d litros de gasolina, el rendimiento es: """ % (kmRecorridos, litrosDeGasolina))
    print("%.2f km/l" % rendimiento)
    print("%.2f mi/gal" % equivalencia)
    kilometrosPorRecorrer = int(input("""
¿Cuántos kilómetros vas a recorrer? """))
    gasolinaNecesaria = calcularGasolina(kilometrosPorRecorrer, rendimiento)
    print("""
Para recorrer %d km. necesitas %.2f litros de gasolina.""" % (kilometrosPorRecorrer, gasolinaNecesaria))


main()