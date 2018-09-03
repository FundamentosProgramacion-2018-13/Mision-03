# Autor: Zoe Caballero Dominguez Matrícula: A01747247
"""Descripción: Este programa calcula el rendiemiento de un auto en kilometros por litro y millas por galón,
leyendo los kilometros recorridos y los litros de gasolina usados. Después pregunta por los kilometros a recorrer y
entrega la cantidad de gasolina a utilizar."""

# Programa

# calularRendimientoKmLitro hace la operación necesaria para sacar el rendimiento en km por litro y lo regresa a main
def calcularRendimientoKmLitro(kmRecorridos, litrosGasolina):
    kmLitro = kmRecorridos / litrosGasolina
    return kmLitro


# calcularRendimientoMillasGalon convierte las unidades y después saca el rendimiento en millas por galon, regresa el resultado a main
def calcularRendimientoMillasGalon(kmRecorridos, litrosGasolina):
    millas = kmRecorridos / 1.6093
    galones = litrosGasolina * 0.264
    millasGalon = millas / galones
    return millasGalon

# calcularGasolina saca los litros de gasolina necesarios para el recorrido en kilometros y regresa el resultado a main
def calcularGasolina(kmViaje, rendimientoKilometros):
    gasolina = kmViaje / rendimientoKilometros
    return  gasolina


# Función main pide los datos, llama a las funciones que calculan el rendimiento y gasolina e imprime los resultados
def main ():
    kmRecorridos = int(input("Teclea el número de km recorridos: "))
    litrosGasolina = int(input("Teclea el número de litros de gasolina usados: "))
    rendimientoKilometros = calcularRendimientoKmLitro(kmRecorridos, litrosGasolina)
    rendimientoMillas = calcularRendimientoMillasGalon(kmRecorridos,litrosGasolina)
    print("\033[1;30m"+"""
Si recorres %d kms con %d litros de gasolina, el rendimiento es:""" % (kmRecorridos, litrosGasolina))
    print("%.2f km/l" % rendimientoKilometros)
    print("""%.2f mi/gal
    """ % (rendimientoMillas))
    kmViaje =  int(input("\033[0;30m"+"¿Cúantos kilometros vas a recorrer? "))
    gasolinaNecesaria = calcularGasolina (kmViaje, rendimientoKilometros)
    print("\033[1;30m"+"""
Para recorrer %d km. necesitas %.2f litros de gasolina""" % (kmViaje, gasolinaNecesaria))

# llamar a main
main()
