# Carlos Badillo García             A01377618
# Programa que lee el número de kilómetro recorridos y la cantidad de gasolina utilizada, además de imprimir el rendimiento del autoomovil (kilómetro/litro y millas/galón)

def calcularRendimientoAutomóvilKmLt(kmRecorridos, litrosGasolina):
    kmLt = kmRecorridos/litrosGasolina
    return kmLt

def convertirKmaMillas(kmRecorridos):
    millas = kmRecorridos/1.6093
    return millas

def convertirLtaGalones(litrosGasolina):
    galones = litrosGasolina * 0.264
    return galones

def litrosNecesarios(kmRecorridos, kmaRecorrer, litrosGasolina):
    litrosNec = (kmaRecorrer*litrosGasolina)/kmRecorridos
    return litrosNec

def main():
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