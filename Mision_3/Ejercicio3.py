# Autor: Roberto Emmanuel González Muñoz
# Escribe un programa que lea las horas normales, las horas extras y el pago por hora de un trabajador.

def calcularNormal(normal,pago):
    pagoNormal = normal*pago
    return pagoNormal


def calcularExtra(extra,pago):
    pagoExtra = extra*(pago*1.85)
    return pagoExtra


def calcularTotal(normal,extra):
    pagoTotal = normal + extra
    return pagoTotal


def main():
    horasNormales = input(int("Escribe las horas normales trabajadas: "))
    horasExtra = input(int("Escribe las horas extra trabajadas: "))
    pagoPorHora = input(int("Teclea el pago por hora: "))
    pagoNormal = calcularNormal(horasNormales,pagoPorHora)
    pagoExtra = calcularExtra(horasExtra,pagoPorHora)
    pagoTotal = calcularTotal(pagoNormal,pagoExtra)
    print("El pago normal es: $%.2f" % pagoNormal)
    print("El pago extra es: $%.2f" % pagoExtra)
    print("El pago extra es: $%.2f" % pagoTotal)


main()