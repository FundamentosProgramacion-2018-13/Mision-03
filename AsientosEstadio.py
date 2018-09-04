# Autor: Luis Ricardo Chagala Cervantes.
# Se calcula el precio total de los boletos de diferentes secciones de un estadio.


# La linea de codigo empieza después de esta linea.

#Se calula el precio de los asientos de la clase A.
def CalcularPrecioA(ClaseA):
    PrecioA = ClaseA * 925
    return PrecioA

#Se calula el precio de los asientos de la clase B.
def CalcularPrecioB(ClaseB):
    PrecioB = ClaseB * 775
    return PrecioB

#Se calula el precio de los asientos de la clase C.
def CalcularPrecioC(ClaseC):
    PrecioC = ClaseC * 360
    return PrecioC

#Se calcula el precio total por todos los aientos.
def CalcularPrecioTotal(PrecioA, PrecioB, PrecioC):
    CostoTotal = PrecioA + PrecioB + PrecioC
    return CostoTotal

def ImprimirResultados(CostoTotal):
    print("El costo total es: %.2f" % (CostoTotal))

def Imprimir(ClaseA, ClaseB, ClaseC):
    PrecioA = CalcularPrecioA(ClaseA)
    PrecioB = CalcularPrecioB(ClaseB)
    PrecioC = CalcularPrecioC(ClaseC)
    PrecioTotal = CalcularPrecioTotal(PrecioA, PrecioB, PrecioC)
    ImprimirResultados(PrecioTotal)

def main():
    ClaseA = int(input("Boletos de la clase A: "))
    ClaseB = int(input("Boletos de la clase B: "))
    ClaseC = int(input("Boletos de la clase C: "))
    Imprimir(ClaseA, ClaseB, ClaseC)


main()