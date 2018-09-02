# Mariana Caballero Cabrera A01376544

# A continuación voy a escribir un programa que calcule la gasoline que necesita según



#esta función calcula el rendimiento en kilometros y litros

def rendimientoKilometros(kilometros, litros):
    rendimientoK = kilometros/litros
    return rendimientoK

#esta función convierte kilometros a millas
def millas (kilometros):
    millasT = kilometros / 1.6093
    return millasT


#esta función convierte litros a galones
def galones (litros):
    galonesT = litros * 0.264
    return galonesT



#esta función calcula el rendimiento en millas y galones
def rendimientoMillas(millasT, galonesT):
    rendimientoM = millasT/galonesT
    return rendimientoM



#esta función imprime
def imprimir (rendimientoK, rendimientoM, kilometros, litros, kilometrosF, rendimientoFuturo):

    print ("Si recorres" , kilometros, "kms con", litros, "litros de gasolina, el rendimiento es: ")
    print ("%5.2f" %(rendimientoK), "km/l")
    print("%5.2f" % (rendimientoM), "mi/gal")
    print ("Para recorrer", kilometrosF,"kms.necesitas","%5.2F"%(rendimientoFuturo),"litros de gasolina")


#esta función calcula los litros de gasolina que necesita en los kilómetros que planea recorrer
def kilometrosFuturo (kilometrosF, rendimientoK):
    rendimientoFuturo = kilometrosF/rendimientoK
    return rendimientoFuturo


#función principal
def main():
    kilometros = int (input( "Teclea el número de kilometros recorridos: "))
    litros = int(input("Teclea el número de litros de gasolina usados: "))
    millasT = millas (kilometros)
    galonesT = galones (litros)
    rendimientoK= rendimientoKilometros (kilometros, litros)
    rendimientoM = rendimientoMillas(millasT, galonesT)
    kilometrosF = int (input( "¿Cuántos kilometros vas a recorrer?: "))
    rendimientoFuturo = kilometrosFuturo (kilometrosF, rendimientoK)
    imprimir(rendimientoK, rendimientoM, kilometros, litros, kilometrosF, rendimientoFuturo)





#llamamos a la función principal
main()
