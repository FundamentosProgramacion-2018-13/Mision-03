# Autor: Roberto Emmanuel González Muñoz
# Escribe un programa que lea el número de kilómetros recorridos y la cantidad de gasolina utilizada

def rendimiento(kilometros,gasolina):
    rendimientoKmL = kilometros / gasolina
    return rendimientoKmL


def rendimientoM(kilometros,gasolina):
    rendimientoMiGal = (kilometros * .6213) / (gasolina * 4.54)
    return rendimientoM


def kmPorRecorrer(kilometros,rend):
    kmXRecorrer = kilometros / rend
    return kmXRecorrer


def main():
    kilometrosRecorridos = input(int("Escribe la cantidad de kilómetros recorridos: "))
    gasolinaUsada = input(int("Escribe la cantidad de gasolina usada: "))
    rendimientoPrevisto = rendimiento(kilometrosRecorridos,gasolinaUsada)
    rendimientoPrevistoM = rendimientoM(kilometrosRecorridos,gasolinaUsada)
    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es: %.2fkm/l o %.2fMi/gal" % (
        kilometrosRecorridos, gasolinaUsada, rendimientoPrevisto, rendimientoPrevistoM))
    kilometrosPrevistos = input(int("Escribe cuántos kilómetros vas a recorrer: "))
    gasolinaPorUsar = kmPorRecorrer(rendimientoPrevisto,kilometrosPrevistos)
    print("Para recorrer %d km. Necesitas %.2f litros de gasolina" % (kilometrosPrevistos,gasolinaPorUsar))


main()