# Autor: Juan Sebastián Lozano Derbez
# Calcula el salario de un empleadp

def calcularpagoNormal(horasnorm, pagoporhor):      #Se calcula el pago en horas normales
    pagonorm = horasnorm * pagoporhor

    return pagonorm

def calcularpagoExtra(horasextra, pagoporhor):      #Se calcula el pago en horas extra
    pagoporextra = pagoporhor + (pagoporhor * .85)
    pagoextra = horasextra * pagoporextra

    return pagoextra

#Se reciben los inputs, se ejecutan las funciones y se suman los resultados de los pagos
def main():
    horasnorm = int(input("Horas normales trabajadas: "))
    horasextra = int(input("Horas extra trabajadas: "))
    pagoporhor = int(input("Pago por hora normal: "))


    pagonorm = calcularpagoNormal(horasnorm, pagoporhor)
    pagoextra = calcularpagoExtra(horasextra, pagoporhor)
    pagototal = pagonorm + pagoextra

    print("Pago normal: $", pagonorm)
    print("Pago extra: $", pagoextra)
    print("------------------------")
    print("Pago total: $", pagototal)

main()