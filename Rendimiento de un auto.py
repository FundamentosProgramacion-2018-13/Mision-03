"""
Nombre: Alexys Martín Coate Reyes
Martícula: A01746998

Descripción: Calcular el la relación distancia/gasolina en km/L y Mi/Gal. Al mismo tiempo calcular la gasoluna necesaria para recorrer cierta distancia.
"""
#Calcula el rendimiento en km/l
def calculoRendimientoKML(kmRec, lGas):
    rendimientoKML = kmRec/lGas
    return rendimientoKML

#Calcula el rendimiento en mi/gal
def calculoRendimientoMG(kmRec, lGas):
    rendimientoMG = (kmRec/1.6093)/(lGas*.264)
    return rendimientoMG

#Imprime los rendimientos en mi/gal y km/L además de esoecificar los km recorridos y la gasolina utilizada
def imprimirRendimiento(kmRec, lGas, rendimientoKML, rendimientoMG):
    print("""Si recorres %.2fkms con %.2fL de gasolina, el rendimiento es:
        %.2f km/l
        %.2f mi/gal""" % (kmRec, lGas, rendimientoKML, rendimientoMG))

#Calcula la gasolina neceesaria para poder recorrer el num. de km deseado
def calcularGas(kmViaje, kmRec, lGas):
    rendmientoKML = calculoRendimientoKML(kmRec, lGas)
    gas = kmViaje/rendmientoKML
    return gas

#Imprimie las gasolina necesaria para poder recorrer el num. de km deseado
def imprimirViaje(kmViaje, gas):
    print("Para recorrer %.2fkm necesitas %.2fL de gasolina" % (kmViaje, gas))

#Función principal que engloba toda la serie de pasos para resolver el resultado. También obtiene los datos de entrada.
def main():
    kmRec = float(input("Teclea el número de km recorridos: "))
    lGas = float(input("Teclea el número de litros de gasolina usados: "))
    rendimientoKML = calculoRendimientoKML(kmRec, lGas)
    rendimientoMG = calculoRendimientoMG(kmRec, lGas)
    imprimirRendimiento(kmRec, lGas, rendimientoKML, rendimientoMG)
    kmViaje = float(input("¿Cuántos kilómetros vas a recorrer? "))
    gas = calcularGas(kmViaje, kmRec, lGas)
    imprimirViaje(kmViaje, gas)

#Ejecuta la función principal
main()