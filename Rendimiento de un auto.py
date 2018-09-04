# Autor: Carlos Alberto Reyes Ortiz
# Te da el rendimiento del automóvil en km/l y mi/gal
# Litros de gasolina que necesitas por kilometros que vayas a recorrer

def calcularRendimiento(kmRecorridos, litrosGasolina): #Da el rendimiento en Km/L

    rendimientoKmEntreL = kmRecorridos / litrosGasolina
    return rendimientoKmEntreL



def transformarKmL_a_MiGal(kmRecorridos, litrosGasolina): #Transforma el rendimiento de km/l a mi/gal

    miRecorridos = ( 1 / 1.6093 ) * kmRecorridos
    galGasolina =   0.264 * litrosGasolina
    rendimientoMiEntreGal = miRecorridos / galGasolina
    return rendimientoMiEntreGal



def calcularLitrosNecesarios(rendimientoKmEntreL, km_a_Recorrer): #Da los litros necesarios dado los km

    litrosNecesarios = km_a_Recorrer / rendimientoKmEntreL
    return litrosNecesarios




def main():  #Función principal: Da rendimiento en km/l y en mi/gal. También te dice cuantos litros de gas necesitas para ciertos kilometros
    kmRecorridos = int(input("Teclea el número de km recorridos: "))
    litrosGasolina = int(input("Teclea el número de litros de gasilina usados: "))
    rendimientoKmEntreL = calcularRendimiento(kmRecorridos, litrosGasolina)
    rendimientoMiEntreGal = transformarKmL_a_MiGal(kmRecorridos, litrosGasolina)
    print("")
    print("Si recorres" ,kmRecorridos, "kms con" ,litrosGasolina, "litros de gasolina, el rendimiento es:")
    print("%.2f" %(rendimientoKmEntreL),"km/l")
    print("%.2f" %(rendimientoMiEntreGal),"mi/gal")
    print()
    km_a_Recorrer = int(input("¿Cuántos kilómetros vas a recorrer? "))
    litrosNecesarios = calcularLitrosNecesarios(rendimientoKmEntreL, km_a_Recorrer)
    print()
    print("Para recorrer" ,km_a_Recorrer, "km. necesitas", "%.2f" %litrosNecesarios, "litros de gasolina" )


main()
