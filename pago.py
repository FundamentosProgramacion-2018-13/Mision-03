def calcularpagoNormal(horasnorm, pagoporhor):
    pagonorm = horasnorm * pagoporhor

    return pagonorm

def calcularpagoExtra(horasextra, pagoporhor):
    pagoporextra = pagoporhor + (pagoporhor * .85)
    pagoextra = horasextra * pagoporextra

    return pagoextra

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