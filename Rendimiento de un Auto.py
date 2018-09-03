# Autor: Juan Carlos Flores García, A01376511

# Descripción: Programa que calcula el rendimiento de un automóvil en kilómetro/litro y millas/galón.
# Después el programa pregunta al usuario la cantidad de kilómetros que va a recorrer e imprime la cantidad de gasolina
# que necesitara.


# La siguiente función calcula el rendimiento de kilómetros/litros.
def calcularRendimientoKmLit(kmRecorridos, litrosDeGasolina):
    rendimiento = kmRecorridos / litrosDeGasolina
    return rendimiento


# La siguiente función convierte kilómetros/litros a millas/galones.
def convierteMillasGalon(rendimientoKmLitro):
    equivalencia = (rendimientoKmLitro / 1.6093) / 0.264
    return equivalencia


# La siguiente función calcula los litros necesarios a recorrer.
def calcularLitrosNecesarios(kmQueRecorrera, rendimientoKmLitro):
    litrosNecesarios = kmQueRecorrera / rendimientoKmLitro
    return litrosNecesarios


# La siguiente función imprime los km recorridos, litros de gasolina, rendimiento km/litro y rendimiento milla/galón.
def imprimir1(kmRecorridos, litrosDeGasolina, rendimientoKmLitro, rendimientoMiGal):
    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es:" % (kmRecorridos, litrosDeGasolina))
    print("%.2f km/l" % rendimientoKmLitro)
    print("%.2f mi/gal" % rendimientoMiGal)


# La siguiente función imprime los km que recorrerá y los litros de gasolina necesarios.
def imprimir2(kmQueRecorrera, litrosNecesarios):
    print("Para recorrer %d km. necesitas %.2f litros de gasolina" % (kmQueRecorrera, litrosNecesarios))


# La función principal lee el valor de km recorridos, litros de gasolina usados y los km a recorrer.
# También calcula el rendimiento de km/litro, milla/galón y los imprime usando sus respectivas funciones.
# Después el programa pregunta la cantidad de km a recorrer, calcula los litros necesarios y los imprime con funciones.
def main():
    kmRecorridos = float(input("Teclea el número de km recorridos: "))
    litrosDeGasolina = float(input("Teclea el número de litros de gasolina usados: "))
    rendimientoKmLitro = calcularRendimientoKmLit(kmRecorridos, litrosDeGasolina)
    rendimientoMiGal = convierteMillasGalon(rendimientoKmLitro)
    imprimir1(kmRecorridos, litrosDeGasolina, rendimientoKmLitro, rendimientoMiGal)
    kmQueRecorrera = float(input("¿Cuántos kilómetros vas a recorrer? "))
    litrosNecesarios = calcularLitrosNecesarios(kmQueRecorrera, rendimientoKmLitro)
    imprimir2(kmQueRecorrera, litrosNecesarios)


# Llama a la función main.
main()
