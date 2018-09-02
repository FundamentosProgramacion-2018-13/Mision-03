# Autor: Alex Serrano Durán
# Este programa checa la eficiencia de gasolina


def calcularMetrico(kilometros, litros):        # Calcula la eficiencia en unidades métricas
    eficienciaMetrico = kilometros / litros
    return eficienciaMetrico


def calcularImperial(kilometros, litros):       # Calcula la eficiencia en unidades imperiales
    eficienciaImp = kilometros/1.6093 / litros/.264
    return eficienciaImp


def calcularLitros(kilometros, litros, kilometrosRecorridos):   # Calcula la gasolina necesaria para recorrer x kms según la eficiencia
    eficiencia = kilometros / litros
    litrosNecesarios = kilometrosRecorridos / eficiencia
    return litrosNecesarios


def main():                     # Función main, pide kilómetros y litros e imprime resultados
    kilometros = int(input("Teclea el número de km recorridos: "))
    litros = int(input("Teclea el número de litros de gasolina usados: "))
    eficienciaMetrico = calcularMetrico(kilometros, litros)
    eficienciaImp = calcularImperial(kilometros, litros)
    print('''
Si recorres %d kms con %d litros de gasolina, el rendimiento es:
%.2f km/l
%.2f mi/gal
''' % (kilometros, litros, eficienciaMetrico, eficienciaImp))
    kilometrosRecorridos = int(input("¿Cuántos kilómetros vas a recorrer? "))
    litrosNecesarios = calcularLitros(kilometros, litros, kilometrosRecorridos)
    print("""
Para recorrer %d km. necesitas %.2f litros de gasolina""" % (kilometrosRecorridos, litrosNecesarios))


main()
