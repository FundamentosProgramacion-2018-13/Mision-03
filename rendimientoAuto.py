# encoding: UTF-8
# Autor: Diego Palmerin Bonada, A01747290
# Descripcion: Calcula el suelo semanal de un trabajador tomando sus horas normales y extras

"""
Análisis:
E: kilometrosRecorridos, gasolinaUtilizada, kilometrosARecorrer
S:kmpl, mpg, litrosParaRecorrerNkm
E/S:
kmpl=kilometrosRecorrodos/gasolinaUtilizada
mpg = (kilometrosRecorridos*1.6093)/(gasolinaUtilizada*0.264)
litrosParaRecorrerNkm =  kilometrosARecorrer/kmpl

Algoritmo:
Ejecutar función main
Obtener del usuario datos de kilómetros recorridos y gasolina utilizada
Ejecutar función kilometrosPorLitro con los datos dados por el usuario
En la función kilometrosPorLitro, dividir kilómetros recorridos entre gasolina utilizada y regresar a main el resultado
De vuelta en main, ejecutar función millasPorGalon con los datos dados por el usuario
En la función millasPorGalon, multiplicar los kilómetros por 1.6093 para convertirlo a millas
Multiplicar los litros por 0.264 para convertirlo a galones
Dividir las millas entre los galones y regresarlo a main para impresión

Preguntar al usuario cuántos kilómetros quiere recorrer
Ejecutar función litrosParaElCamino con el último dato dado por el usuario y con la variable kmpl
Dividir los kilómetros que quiere recorrer el usuario y dividirlo entre los kilómetros por litro que rinde el coche
Regresar resultado a main e imprimirlo
"""


#Calcular en rendimiento del auto en km/l
def kilometrosPorLitro(km, l):
    return km/l


#Calcular en rendimiento del auto en mi/gal
def millasPorGalon(km, l):
    kmAmi = km / 1.6093
    lAga = l * 0.264
    return kmAmi / lAga


#Calcular los litros necesarios para recorrer ciertos km
def litrosParaElCamino(km, kmpl):
    return km/kmpl


#Multiplicar las horas extra por 185% del sueldo normal por hora
def main():
    kilometros = float(input("Teclea el número de km recorridos: "))
    litros = float(input("Teclea el número de litros de gasolina usados: "))
    print("")
    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es: " % (kilometros, litros))
    kmpl = kilometrosPorLitro(kilometros, litros)
    print("%.2f km/l" % kmpl)
    print("%.2f mi/gal" % millasPorGalon(kilometros, litros))
    print("")
    kilometrosARecorrer = float(input("¿Cuántos kilómetros vas a recorrer? "))
    print("")
    print("Para recorrer %d km. necesitas %.2f litros de gasolina" % (kilometrosARecorrer, litrosParaElCamino(kilometrosARecorrer, kmpl)))


main()
