#Autor: Alan Diaz Carrera
#Descripción: Calcular el rendimiento de un auto

km = int(input("Teclea el numero de kilometros recorridos:"))
lit = int(input("Tecle el numero de litros de gasolina usados:"))

#Calcular rendimiento
def calcular(km, lit):
    kmL=km/lit
    milGal=(km*1.6093)/(lit*0.264)
    print("Si recorres %3.0f kms con %2.0f litros de gasolina, el rendimiento es:" % (km, lit))
    print("%.2f km/l" % (kmL))
    print("%.2f mi/gal" % (milGal))
    return kmL
#Calcular cuantos litros se necesitan
def main():
    kmetro = calcular(km, lit)
    recor = int(input("Cuantos kilometros vas a recorrer?"))
    necesidad = recor / kmetro
    print("Para recorrer %.1f km. necesitas %.2f litros de gasolina" % (recor, necesidad))

main()