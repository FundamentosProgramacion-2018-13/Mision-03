#Irma Gómez Carmona
#Calcular el rendimeitno de un auto en KM/L y hacer la conversion de MI/GAL. Además de calcular cuantos litros se
#necesitan para recorrer la distancia introducida por el usuario

def calcularRendimiento(km, l):
    rendimiento=km/l
    return rendimiento
def calcularRendimientoConversion (km,l):
    rendimiento2=(km/1.6093)/(l*0.264)
    return rendimiento2
def calcularKilometros(km,l,distancia):
    litros=distancia*l/km
    return litros
def main ():
    kilometros=int(input("Teclea el número de km recorridos: "))
    litros = int(input("Teclea el número de litros de gasolina usados: "))
    km=calcularRendimiento(kilometros,litros)
    l=calcularRendimientoConversion(kilometros,litros)
    print("""
    Si recorres %d kms con %d litros de gasolina, el rendimiento es: 
    %.2f km/l
    %.2f mi/gal
    """%(kilometros,litros,km,l))
    kmViajar=int(input("¿Cuantos kilometros va a recorrer? "))
    distancia=calcularKilometros(kilometros,litros,kmViajar)
    print("""
    Para recorrer %d km necesitas %.2f litros de gasolina"""%(kmViajar,distancia))

main()
