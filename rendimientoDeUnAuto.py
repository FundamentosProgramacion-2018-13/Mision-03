#Autor: Jesus Zabdiel Sanchez Chavez A01374964

#Descripcion: Programa que calcula el rendimiento de un automovil en kilometros por litro y millas por galon tomando
#tomando en cuenta los kilometros recorridos y la gasolina utlizada.


#funcion principal
def main ():
    kilometros = int(input("Escribe el número de kilometros que recorriste: "))
    gasolina  = int (input("Escriba la cantidad de gasolina utlizada en litros: "))
    rendimientoKm = calcularRendimientoKm(kilometros, gasolina)
    rendimientoMi = calcularRendimientoMi(kilometros, gasolina)
    print ('''Si recorres %d kms con %d litros de gasolina, el rendimiento es:
    %.2f km/l
    %.2f mi/gal ''' % (kilometros,gasolina, rendimientoKm,rendimientoMi))
    kilometrosRecorrer = int(input("¿Cuántos kilómetros vas a recorrer?: "))
    gasolinar = calcularGasolina(rendimientoKm, kilometrosRecorrer)
    print ("Para recorrer %d km. necesitas %.2f litros de gasolina" %(kilometrosRecorrer, gasolinar))




#calcula el rendimiento del carro en kilometros por litro
def calcularRendimientoKm (kilometros, gasolina):
    rendimientoKm = kilometros / gasolina
    return  rendimientoKm

#Convierte los kilometros a millas y los litros a galones y callcula el rendimiento con estas unidades.
def calcularRendimientoMi(kilometros, gasolina):
    rendimientoMi = (kilometros / 1.6093) / (gasolina * .264)
    return rendimientoMi


#Calcula la gasolina nbecesaria para recorrer ciertos kilometros
def calcularGasolina (rendimientoKm, kilometrosRecorrer):
    gasolinar = kilometrosRecorrer / rendimientoKm
    return gasolinar

main()