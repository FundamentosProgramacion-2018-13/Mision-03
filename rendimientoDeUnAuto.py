#Autor Claudio Mayoral García
#Descripción: Pedirá el número de km recorridos, los litros de gasolina usados y los kilómetros que quiere recorrer
# e imprime el rendimiento del automovil y la cantidad de gasolina que utilizará



def calcularRendimientoKmLit(kmRecorridos, litrosDeGasolina):
    #Calcula el rendimiento del auto con una fórmula
    #Regresa el rendimiento
    rendimiento = kmRecorridos / litrosDeGasolina
    return rendimiento


def calcularEquivalenciaMillasGalon(rendimientoKmLit):
    #Calcula la quivalencia de km/l y mi/gal con una fórmula
    #Regresa la equivalencia
    equivalencia = rendimientoKmLit / 1.6093 / 0.264
    return equivalencia


def calcularLitrosNecesarios(kmQueRecorrera, rendimientoKmLit):
    #Calcula los litros necesarios para ciertos kilómetros
    #Regresa los litrosNecesarios
    litrosNecesarios = kmQueRecorrera / rendimientoKmLit
    return litrosNecesarios


def main():
    #kmRecorridos = Lee los kilómetros recorridos
    #litrosDeGasolina = Lee los litros de gasolina
    #rendimientoKmLit = calcula el rendimiento con kilómetros por litro
    #rendimientoMiGal = calcula el rendimiento con millas por galón
    #kmQueRecorrera = Lee los kilómetros que recorrerá
    #Imprime de acuerdo al formato establecido
    kmRecorridos = float(input("Teclea el número de km recorridos: "))
    litrosDeGasolina = float(input("Teclea el número de litros de gasolina usados: "))
    rendimientoKmLit = calcularRendimientoKmLit(kmRecorridos, litrosDeGasolina)
    rendimientoMiGal = calcularEquivalenciaMillasGalon(rendimientoKmLit)
    print("")
    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es:" % (kmRecorridos, litrosDeGasolina))
    print("%.2f km/l" % rendimientoKmLit)
    print("%.2f mi/gal" % rendimientoMiGal)
    print("")
    kmQueRecorrera = float(input("¿Cuántos kilómetros vas a recorrer? "))
    litrosNecesarios = calcularLitrosNecesarios(kmQueRecorrera, rendimientoKmLit)
    print("")
    print("Para recorrer %d km. necesitas %.2f litros de gasolina" % (kmQueRecorrera, litrosNecesarios))


#Llama a la función "main"
main()
