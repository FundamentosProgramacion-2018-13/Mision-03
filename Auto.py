# Autor: Silvia Ferman Muñoz
# Programa que calcule el rendimiento y gasolina utilizadad de un auto
# Demo Top-Down

def calcularRendimiento(kmRecorridos, litrosGas):
    rendimiento = kmRecorridos / litrosGas
    return rendimiento


# Calcula el valor que equivale a millas/galon del rendimiento
def calcularEquivalencia(rendimiento):
    equivalencia = rendimiento / 1.6093 / 0.264
    return equivalencia


# Se calcula la cantidad de gal¡solina que se utiliza
def calcularGasolina(kmPorRecorrer, rendimiento):
    gasNecesaria = kmPorRecorrer / rendimiento
    return gasNecesaria


# Funcion principal
def main():
    kmRecorridos = int(input("Teclea el número de km recorridos:"))
    litrosGas = int(input("Teclea el número de litros de gasolina usados:"))
    rendimiento = calcularRendimiento(kmRecorridos, litrosGas)
    equivalencia = calcularEquivalencia(rendimiento)
    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es:" % (kmRecorridos, litrosGas))
    print("%.2f km/l" % rendimiento)
    print("%.2f mi/gal" % equivalencia)
    kmPorRecorrer = int(input("¿Cuántos kilómetros vas a recorrer?:"))
    gasNecesaria = calcularGasolina(kmPorRecorrer, rendimiento)
    print("Para recorrer %d km. necesitas %.2f litros de gasolina:" % (kmPorRecorrer, gasNecesaria))

main()
