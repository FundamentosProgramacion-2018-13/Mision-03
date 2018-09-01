#Autor: Arturo Márquez Olivar. A01376086
#Calcula el rendimiento de un auto.

#Esta función calcula el rendimiento en km/lt.
def calcularRendimientoKm(kilometrosRecorridos, gasolinaUsada):
    rendimientoKm= kilometrosRecorridos / gasolinaUsada
    return rendimientoKm
    
#Esta función calcula el rendimiento en mi/gal.    
def calcularRendimientoMillas(kilometrosRecorridos, gasolinaUsada):
    millas= kilometrosRecorridos / 1.6093
    galones= gasolinaUsada * 0.264
    rendimientoMillas= millas / galones
    return rendimientoMillas
    
#Esta función calcula la gasolina necesaria según los kilometros a recorrer.    
def calcularGasNecesaria(rendimientoKm, kmPorRecorrer):
    gasNecesaria= kmPorRecorrer / rendimientoKm
    return gasNecesaria
 
#Función principal, se encarga de leer y de imprimir los datos.
def main():
    kilometrosRecorridos= float(input("¿Teclea el número de kilometros recorridos."))
    gasolinaUsada= float(input("Teclea los litros de gasolina que fueros utilizados."))
    
    rendimientoKm= calcularRendimientoKm(kilometrosRecorridos, gasolinaUsada)
    rendimientoMillas= calcularRendimientoMillas(kilometrosRecorridos, gasolinaUsada):
    
    print("""Si recorriste %.1f km. con %.1f litros de gasolina, el rendimiento del auto es de: 
             %.2f km/lt
             %.2f mi/gal""" % (kilometrosRecorridos, gasolinaUsada, rendimientoKm, rendimientoMillas))
             
    kmPorRecorrer= float(input("¿Cuántos kilometros vas a recorrer?")
    
    gasNecesaria= calcularGasNecesaria(rendimientoKm, kmPorRecorrer)
    
    print("Para poder recorrer %.1f km, necesitas %.2f de gasolina." % (kmPorRecorrer, gasNecesaria))
    
#Llamada a la función principal.  
main()
