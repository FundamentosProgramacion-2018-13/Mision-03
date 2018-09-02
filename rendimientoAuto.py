#Autor: Víctor Manuel Rodríguez Loyola A01747755
#Descripción: Este programa calcula el rendimiento de un auto en km/litro y millas/galón


def calcularRendimientoKmL(km, lts): #Calcula el rendimiento del auto en Km/L
    rendimientoKmL= km/lts
    return rendimientoKmL


def calcularRendimientoMiGal(km, lts): #Convierte el rendimiento del auto en k/L a mi/gal
    rendimientoMiGal = calcularRendimientoKmL(km, lts)/1.6093/0.264
    return rendimientoMiGal


def calcularLtsNecesarios(kmARecorrer): #Calcula los litros necesarios para recorrer los kilómetros que indica el usuario
    ltsNecesarios= kmARecorrer/27.94
    return ltsNecesarios


def main():
    kmRecorridos= int(input("Teclea el número de km recorridos: "))
    ltsUsados= int(input("Teclea el número de litros de gasolina usados: "))
    rendimientoKmL= calcularRendimientoKmL (kmRecorridos, ltsUsados)
    rendimientoMiGal = calcularRendimientoMiGal (kmRecorridos, ltsUsados)
    print("Si recorres",kmRecorridos,"kms con",ltsUsados,"litros de gasolina, el rendimiento es:")
    print("%.2f km/l" % (rendimientoKmL))
    print("%.2f mi/gal" % (rendimientoMiGal))
    kmPorRecorrer= int(input("\n¿Cuántos kilómetros vas a recorrer? "))
    ltsNecesarios= calcularLtsNecesarios(kmPorRecorrer)
    print("Para recorrer %d km necesitas %.2f litros de gasolina" %(kmPorRecorrer,ltsNecesarios))


main()


