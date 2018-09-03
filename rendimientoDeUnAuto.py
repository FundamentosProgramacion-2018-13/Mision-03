#Autor: Michelle Sánchez Guerrero
#Descripción: Programa que calcula el rendimiento de un auto.

#Función que calcula el rendimiento del auto en km/l
def calcularRendimiento(distancia, gasolina):
    rendimiento = distancia / gasolina
    return rendimiento
    
#Función que calcula el rendimiento del auto en mi/gal
def calcularRendimientoMillas(kilometros, litros):
    millas = kilometros / 1.6093
    galones = litros * 0.264
    rendimientoMillas = calcularRendimiento(millas, galones)
    return rendimientoMillas

#Función que calcula los litros de gasolina necesarios para recorrer una distancia.
def calcularLitrosGasolina(kilometros, litros, futurosKm):
    rendimiento = calcularRendimiento(kilometros, litros)
    gasolina = futurosKm / rendimiento
    return gasolina

#Función principal. Lee datos e imprime datos.
def main():
    kilometros = int(input('''Teclea el número de km recorridos: '''))
    litros = int(input("Teclea el número de litros de gasolina usados: "))
    print()
    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es:" % (kilometros, litros))
    print("%.02f km/l" % (calcularRendimiento(kilometros, litros)))
    print("%.02f mi/gal" % (calcularRendimientoMillas(kilometros, litros)))
    print()
    futurosKm = int(input("¿Cuántos kilómetros vas a recorrer? "))
    litrosNecesarios = calcularLitrosGasolina(kilometros, litros, futurosKm)
    print()
    print("Para recorrer %d km. necesitas %.02f litros de gasolina" % (futurosKm, litrosNecesarios))

#Llamar a la función principal
main()