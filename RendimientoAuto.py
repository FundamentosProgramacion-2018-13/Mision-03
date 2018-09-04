# Autor: Luis Ricardo Chagala Cervantes.
# Calcular el rendimiento de un auto en Km/H y Mi/Gal, respecto a las gasolina utilizada y la distancia ya recorrida.


# La linea de codigo empieza después de esta linea.

#Se calculara los km/l del auto.
def calcularRendimiento(Kilometros, Gasolina):
    kmporLitro = Kilometros / Gasolina
    return kmporLitro

#Se tranforma de km/l a mi/gal.
def calcularTransformacion(Kilometros, Gasolina):
    Mi = Kilometros / 1.6093
    Gal = Gasolina * 0.264
    MiporGalon = Mi / Gal
    return MiporGalon

#Se imprimen los km/l y mi/gal.
def ImprimirResultados(kmporLitro ,MiporGalon):
    print("De acuerdo a lo anotado el auto tendra el siguiente rendimiento:")
    print("%.2f Km/l " % (kmporLitro))
    print("%.2f mi/gal" % (MiporGalon))


def Imprimir(Kilometros, Gasolina):
    kmporLitro = calcularRendimiento(Kilometros, Gasolina)
    MiporGalon = calcularTransformacion(Kilometros, Gasolina)
    ImprimirResultados(kmporLitro, MiporGalon)

#Se realiza una regla de tres para calcular la gasolina necesaria.
def calcularGasolina(Necesidad, Kilometros, Gasolina):
    GasolinaNecesitada = (Necesidad * Gasolina) / Kilometros
    return GasolinaNecesitada

#Se imprime el la Gasolina a ocupar.
def ImprirmirNecesito(GasolinaNecesitada, Necesidad):
    print("Necesitas %.2f litros de gasolina para recorrer los %.0f kilometros." % (GasolinaNecesitada, Necesidad))


def Impri(Necesidad, Kilometros, Gasolina):
    GasolinaNecesitada = calcularGasolina(Necesidad, Kilometros, Gasolina)
    ImprirmirNecesito(GasolinaNecesitada, Necesidad)

def main():
    Kilometros = int(input("Kilometros Recorridos: "))
    Gasolina = int(input("Gasolina utilizada: "))
    Imprimir(Kilometros, Gasolina)
    Necesidad = int(input("¿Cuántos kilómetros vas a recorrer? "))
    Impri(Necesidad, Kilometros, Gasolina)

main()
