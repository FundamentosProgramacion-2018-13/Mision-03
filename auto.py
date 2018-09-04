def calcularRendimientolit(km, l):
    rendlit = km/l
    return rendlit

def calcularRendimientogal(km, l):
    mill = km / 1.6093
    gal = l *.264

    rendmill = mill/gal
    return rendmill

def calcularLitros(rendlit, dist):
    litrosnec = dist/rendlit
    return litrosnec

def main():
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