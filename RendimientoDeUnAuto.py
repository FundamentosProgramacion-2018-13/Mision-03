#Damián Iván García Ravelo
#A01376354
#Programa que calcula el rendimiento de un auto

def rendimientoKmEntreLitro (kilometros, litros): #Calcula el rendimiento de kilómetro por litro
    rendimientoKmLitro = kilometros / litros
    return rendimientoKmLitro

def rendimientoMillaEntreGalón (kilometros, litros): #Calcula el rendimiento de milla por galón
    galon = litros * 0.264
    millakm = 1 / 1.6093
    milla = kilometros * millakm
    rendimientoMillaGalon = milla/ galon
    return rendimientoMillaGalon

def kilometroLitro (kilometrosRecorrer, rendimientoKmLitro): #El km/l obtenido lo divide entre los kilómetros que el usuario desea recoorer
    litrosUsar = kilometrosRecorrer/rendimientoKmLitro
    return litrosUsar

def main ():
#Pregunta al usuario los kilometros y los litros usados
    kilometros = (int(input("Teclea el número de kilometros recorridos: ")))
    litros = (int(input("Teclea el número de litros consumidos: ")))
#Define a las variables con su respectiva función
    rendimientoKmLitro = rendimientoKmEntreLitro(kilometros, litros)
    rendimientoMillaGalon = rendimientoMillaEntreGalón(kilometros, litros)
#Imprime el rendimiento en km/l y en mi/gal
    print ("Si recorres" ,kilometros, "kms con", litros, "litros de gasolina, el rendimiento es:")
    print ( format(rendimientoKmLitro, ".2f"), "km/l")
    print (format(rendimientoMillaGalon, ".2f"), "mi/gal")
#Pregunta al usuario los kilometros que desa recorrer
    kilometrosRecorrer = int(input("¿Cuántos kilometros vas a recorrer?: "))
#Asigna a la variable con su función
    litrosUsar = kilometroLitro(kilometrosRecorrer, rendimientoKmLitro)

#Imprime la gasolina requerida para recorrer los kilometros deseados
    print ("Para recorrer",kilometrosRecorrer, "km. necesitas", format(litrosUsar, ".2f"), "litros de gasolina" )
main () #Llama a la función principal