#Autor: Samantha MArtínez Franco
#Descripción: Calcular el rendimiento de un auto de acuerdo a el numero de km y los litros de gasolina
#y que diga cuantos litros de gasolina vas a ocupar de acuerdo a los kilometros que quieres recorrer

def calcularRendimiento(km,litros):   #función que calcula el rendimiento en km/lt
    kmLt=km/litros
    return kmLt

def hacerConversion(km,litros):   #función que  hace la conversión del rendimiento a mil/gal
    milgal=calcularRendimiento(km,litros)/1.6093/0.264
    return milgal

def imprimirLitrosNecesarios(kmRecorridos,kmLt):   #función que calcula los litros necesarios para recorrer los kilometros
    litrosNecesarios=kmRecorridos/kmLt
    return litrosNecesarios



def main():     #función principal
    km=int(input("Teclea el número de km recorridos: "))    #pedir datos para rendimiento
    litros=int(input("Teclea el número de litros de gasolina usados: "))
    rendimiento=calcularRendimiento(km,litros)   #llama rendimiento
    conversion=hacerConversion(km,litros)    #llama a la conversión de rendimiento
    print("Si recorres",km,"con ",litros,'''litros de gasolina el rendimiento es: ''')  #imprime resultados de rendimiento
    print("%.2f " % (rendimiento),"km/l")
    print('''%.2f ''' % (conversion),"mi/gal")
    kmRecorridos=int(input("¿Cuántos kilómetros vas a recorrer?"))  #lee valor de kilometros a recorrer
    litrosNecesario=imprimirLitrosNecesarios(kmRecorridos,rendimiento)    #llama a función que calcula los litros
    print('''Para recorrer ''',kmRecorridos,'''km, necesitas %.2f '''% (litrosNecesario),"litros de gasolina")   # imprime resultados




#llamar función principal
main()