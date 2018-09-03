#Autor: David Rodriguez
#Con el número de kilómetros recorridos y la cantidad de gasolina utilizada
#Imprime el rendimiento de un automóvil en kilómetros/litro y millas/galón
#Al final pregunta cuántos kilómetros se viajarán e imprime los litros de gasolina necesarios

#Calcula la cantidad de litrs necesatrios para recorrer la distancia proporcionada
def calcularLitrosNecesarios(kilometrosARecorrer, kilometrosPorLitro):
    litrosNecesarios = kilometrosARecorrer/kilometrosPorLitro
    return litrosNecesarios


#Calcula el rendimiento en millas por galón (mi/gal)
def calcularMillasPorGalon(kilometrosRecorridos,litrosUsados):
    millasPorGalon = (kilometrosRecorridos/litrosUsados)*2.35397
    return millasPorGalon



#Calcula el rendimiento en kilómetros por litro (km/l)
def calcularKilometrosPorLitro(kilometrosRecorridos, litrosUsados):
    kilometrosPorLitro = kilometrosRecorridos/litrosUsados
    return kilometrosPorLitro

#Imprime los kilómetros por litro y las millas por galón
def imprimir(kilometrosPorLitro, millasPorGalon, kilometrosRecorridos, litrosUsados):
    print("Si recorres", kilometrosRecorridos,"kms con", litrosUsados, "litros de gasolina, el rendimiento es: ")
    print("%.2f"%kilometrosPorLitro, " km/l")
    print("%.2f"%millasPorGalon," mi/gal")

#Imprime los litros necesarios para recorrer la distancia solicitada
def imprimir2(litrosNecesarios, kilometrosARecorrer):
    print("Para recorrer", kilometrosARecorrer, "necesitas%.2f"% litrosNecesarios, "litros de gasolina")


def main():
    kilometrosRecorridos = int(input("Teclea el número de km recorridos: "))
    litrosUsados = int(input("Teclea el número de litros de gasolina usados: "))
    kilometrosPorLitro = calcularKilometrosPorLitro(kilometrosRecorridos, litrosUsados)
    millasPorGalon = calcularMillasPorGalon(kilometrosRecorridos, litrosUsados)
    imprimir(kilometrosPorLitro, millasPorGalon, kilometrosRecorridos, litrosUsados)
    kilometrosARecorrer = int(input("¿Cuántos kilómetros vas a recorrer? "))
    litrosNecesarios = calcularLitrosNecesarios(kilometrosARecorrer, kilometrosPorLitro)
    imprimir2(litrosNecesarios, kilometrosARecorrer)

#Llama a la función principal
main()