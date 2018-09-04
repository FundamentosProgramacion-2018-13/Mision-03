# Carlos Badillo García             A01377618
# Programa que lee el número de kilómetro recorridos y la cantidad de gasolina utilizada, además de imprimir el rendimiento del autoomovil (kilómetro/litro y millas/galón)

def calcularRendimientoAutomóvilKmLt(kmRecorridos, litrosGasolina): #Función que sirve para calcular el rendimiento del auto en km sobre litros
    kmLt = kmRecorridos/litrosGasolina
    return kmLt

def convertirKmaMillas(kmRecorridos): #Función que sirve para convertir km en millas
    millas = kmRecorridos/1.6093
    return millas

def convertirLtaGalones(litrosGasolina): #Función que sirve para convertir litros en galones
    galones = litrosGasolina * 0.264
    return galones

def litrosNecesarios(kmRecorridos, kmaRecorrer, litrosGasolina): #Función que sirve para obtener los litros necesario para recorrer cierta distancia
    litrosNec = (kmaRecorrer*litrosGasolina)/kmRecorridos
    return litrosNec

def main(): #Función principal que sirve para pedirle al usuario los km recorridos, los l de gasolina y los km por recorrer, tambén imrpime valores.
    kmRecorridos = int(input("Teclea el número de km recorridos: "))
    litrosGasolina = int(input("Teclea el número de litros de gasolina usados: "))
    print()
    print("Si recorres", kmRecorridos, "kms con", litrosGasolina, "litros de gasolina, el rendimientos es:")
    print("%.2f" %calcularRendimientoAutomóvilKmLt(kmRecorridos, litrosGasolina),"km/l")
    rendMiGal = convertirKmaMillas(kmRecorridos)/convertirLtaGalones(litrosGasolina)
    print("%.2f" %rendMiGal, "mi/gal")
    print()
    kmaRecorrer = int(input("¿Cuántos kilómetros vas a recorrer?"))
    print()
    print("Para recorrer", kmaRecorrer, "km. necesitas %.2f" %litrosNecesarios(kmRecorridos, kmaRecorrer, litrosGasolina), "litros de gasolina")

main()