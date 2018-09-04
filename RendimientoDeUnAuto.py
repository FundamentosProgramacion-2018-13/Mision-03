# Autor: Luis Armando Miranda Alcocer
# Determinar rendimiento de un auto teniendo kilómetros recorridos, litros de gasolina usado y kilometros a recorrer.

def calcularRendimientoKmLitros (kilometrosRecorridos, litrosUsados):
    rendimientoKilometrosLitro = kilometrosRecorridos/litrosUsados
    return rendimientoKilometrosLitro

def calcularRendimientoMillasGalones (kilometrosRecorridos, litrosUsados):
    rendimientoKilometrosLitro = kilometrosRecorridos / litrosUsados #Se dividen para sacar rendimiento
    rendimientoMillasGalones= rendimientoKilometrosLitro/(1.6093*0.264) #Se calcula un factor de conversión, de km a millas y de litros a galones.
    return rendimientoMillasGalones


def main():
    kilometrosRecorridos = int(input("Teclea el número de km recorridos: "))
    litrosUsados = int(input("Teclea el número de litros de gasolina usados: "))
    rendimientoKilometrosLitro = calcularRendimientoKmLitros (kilometrosRecorridos, litrosUsados)
    print ()
    print ("Si recorres ",(kilometrosRecorridos), " kms con ",(litrosUsados)," litros de gasolina, el rendimiento es: ")
    print ("%.2f" %rendimientoKilometrosLitro, "km/l")
    rendimientoMillasGalones = calcularRendimientoMillasGalones(kilometrosRecorridos, litrosUsados)
    print ("%.2f" %rendimientoMillasGalones, "mi/gal") #Se conviertan a millas y galones.
    print()
    kilometrosPorRecorrer = int(input("¿Cuántos kilómetros vas a recorrer?: "))
    print()
    print ("Para recorrer", (kilometrosPorRecorrer),"km. necesitas %.2f" %(kilometrosPorRecorrer/rendimientoKilometrosLitro), "litros de gasolina")
main()