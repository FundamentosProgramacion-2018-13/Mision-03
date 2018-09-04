# Autor: David Isaí López Jaimes
# A01748363
# Calcula dependiendo lo que hayas recorrido, la gasolina que gastarás

def rendimientoAuto(km, L):
    rendimiento = km / L
    return rendimiento

def conversion(km, L):
    millasGalones = km / 1.6093
    millasGalones = millasGalones / (L/0.264)
    return millasGalones

def main():

    kmRecorridos = int(input("Teclea el numero de Km recorridos: "))
    litrosUtilizados = int(input("Teclea el numero de litros de gasolina usados: "))

    rendimiento = rendimientoAuto(kmRecorridos, litrosUtilizados)
    rendimientoMillas = conversion(kmRecorridos, litrosUtilizados)

    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es: " % (kmRecorridos, litrosUtilizados))
    print(format(rendimiento, ".2f"),"km/l")
    print(format(rendimientoMillas, ".2f"), "mi/gal")


main()
