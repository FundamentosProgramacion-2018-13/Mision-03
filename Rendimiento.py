#Autor: Daniel Cordova Bermudez
#Descripción: En este programa calcula el rendimiento de un auto

def calcularRendimientoKm(kmRecorridos, litrosdeGasolina):
    rendimiento = kmRecorridos/litrosdeGasolina
    return rendimiento

def calcularRendimientoMi(kmRecorridos, litrosdeGasolina):
    rendimientokm = calcularRendimientoKm(kmRecorridos, litrosdeGasolina)
    rendimientoMi = rendimientokm/(1.6093*0.264)
    return rendimientoMi

def calcularLitrosNecesarios (kmRecorridos, litrosdeGasolina, kmPorRecorrer):
    rendimiento = calcularRendimientoKm(kmRecorridos, litrosdeGasolina)
    litrosNecesarios = kmPorRecorrer/rendimiento
    return litrosNecesarios

def main():
    kmRecorridos = int(input("Teclea el número de km recorridos: "))
    litrosGasolinaUsados = int(input("Teclea el número de litros de gasolina usados: "))

    rendimientoKmL = calcularRendimientoKm (kmRecorridos, litrosGasolinaUsados)
    rendimientoMiG = calcularRendimientoMi (kmRecorridos, litrosGasolinaUsados)

    print("")
    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es: " %(kmRecorridos, litrosGasolinaUsados))
    print("%.2f km/l" %(rendimientoKmL))
    print("%.2f mi/gal" %(rendimientoMiG))
    print("")
    kmPorRecorrer = int(input("¿Cuántos kilómetros vas a recorrer?"))
    litrosAUsar = calcularLitrosNecesarios(kmRecorridos, litrosGasolinaUsados, kmPorRecorrer)
    print("")
    print("Para recorrer %d km. necesitas %.2f litros de gasolina" %(kmPorRecorrer, litrosAUsar))

main()



