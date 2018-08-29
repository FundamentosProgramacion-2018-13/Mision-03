# Author: Ivan Honc Ayón     A01376466       Grupo 2
# Descripción: Este programa calcula el rendimiento de un auto.


#Esta función divide los kilometros entre los litros de gasolina para sacar el rendimiento en km/l.
def metroLitro(kilometros, gasolina):
    rendimientoKmts = kilometros/gasolina

    return rendimientoKmts


#Esta función manda a llamar a la función anterior para usar el rendimiento en km/l y lo multiplica para sacar la conversión y calcularlo en mi/gal.
def millaGalon(kilometros, gasolina):
    rendimientoMillas = (metroLitro(kilometros, gasolina))*(1/(1.6093*0.264))

    return rendimientoMillas

#Esta función divide los kilómetros por recorrer entre el rendimiento en kilómetros para calcular los litros requeridos.
def necesitaLitro(kilometros, gasolina, kmPorRecorrer):
    necesita = kmPorRecorrer/(metroLitro(kilometros, gasolina))

    return necesita

#Esta es la función principal para recibir los valores del usuario y llamar al resto de las funciones.
def main():
    km = float(input("Teclea el número de km recorridos: "))
    gas = float(input("Teclea el número de litros de gasolina usados: "))
    rendkm = metroLitro(km, gas)
    rendmilla = millaGalon(km, gas)

    print("""
Si recorres %d kms con %d litros de gasolina, el rendimiento es:
%.2f km/l
%.2f mi/gal""" % (km, gas, rendkm, rendmilla))

    kmFaltantes = float(input("""
¿Cuántos kilómetros vas a recorrer? """))
    litrosFaltantes = necesitaLitro(km, gas, kmFaltantes)

    print("""
Para recorrer %d km. necesitas %.2f litros de gasolina""" % (kmFaltantes, litrosFaltantes))


main()
