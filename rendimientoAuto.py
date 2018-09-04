#Jocelyn López Ortíz A01377451
#Cálculo del rendimiento de un auto en kilometros por litro y millas por galón

def calculoDelRendimientoKilometros(kilometros, gasolina):
    rendimientoKL = kilometros/gasolina
    return rendimientoKL

def calculoDelRendimientoGalones(km, gasolina):
    rendimientoKm = calculoDelRendimientoKilometros(km, gasolina)
    rendimientoGl = rendimientoKm/(1.6093*0.264)
    return rendimientoGl

def calculoDeGasolinaNecesaria(km, gasolina, kmARecorrer):
    rendimiento = calculoDelRendimientoKilometros(km,gasolina)
    gasolinaNecesaria = kmARecorrer/rendimiento
    return gasolinaNecesaria

def main():
    kmRecorridos = int(input("Teclea el numero de km recorridos: "))
    litrosGasolina = int(input("Teclea el número de litros de gasolina usados: "))
    rendimientoKm = calculoDelRendimientoKilometros(kmRecorridos, litrosGasolina)
    rendimientoMi = calculoDelRendimientoGalones(kmRecorridos, litrosGasolina)
    print()
    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es:" %(kmRecorridos, litrosGasolina))
    print("%.2f km/l" %(rendimientoKm))
    print("%.2f mi/gal" %(rendimientoMi))
    print()
    kmARecorrer = int(input("¿Cúantos kilómetros vas a recorrer? "))
    litrosNecesarios = calculoDeGasolinaNecesaria(kmRecorridos,litrosGasolina, kmARecorrer)
    print()
    print("Para recorrer %d km. necesitas %.2f litros de gasolina" %(kmARecorrer, litrosNecesarios))


main()
