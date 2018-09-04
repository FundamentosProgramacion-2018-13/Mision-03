# Autor: Juan Sebastián Lozano Derbez
# Se calcula el rendimiento del carro y la gasolina necesaria para recorrer una distancia

def calcularRendimientolit(km, l):      #Se hace el cálculo del rendimiento en litros
    rendlit = km/l
    return rendlit

def calcularRendimientogal(km, l):      #Se hace el cálculo del rendimiento en galones
    mill = km / 1.6093
    gal = l *.264

    rendmill = mill/gal
    return rendmill

def calcularLitros(rendlit, dist):      #Se calculan los litros necesarios en base al rendimiento
    litrosnec = dist/rendlit
    return litrosnec

def main():                             #Función que recibe los inputs y ejecuta las funciones
    km = int(input("Numero de kilometros recorridos: "))
    l = int(input("Numero de litros de gasolina usados: "))

    rendlit = calcularRendimientolit(km, l)
    rendgal = calcularRendimientogal(km, l)

    print("Si recorres", km, " km con", l, "litros de gasolina, tu rendimiento es de:")
    print("%.2f" %rendlit, "km/l")
    print("%.2f"%rendgal, "mi/gal")

    dist = int(input("Distancia que se desea recorrer (km): "))
    litrosnec = calcularLitros(rendlit, dist)

    print("Se necesitarán %.2f" % litrosnec, "litros para recorrer", dist, "km")

main()