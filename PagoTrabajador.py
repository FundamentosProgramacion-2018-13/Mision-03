# Autor: Silvia Ferman Muñoz
# Programa que lee las horas normales, extras y pago por hr. de un trabajador en una semana.
# Demo Top-Down


#
def calcularPagoNormal(normales, hora):
    pagoNormal = normales * hora
    return pagoNormal


def calcularPagoExtra(extras, hora):
    pagoExtra = extras * (hora * 1.85)
    return pagoExtra


def main():
    normales = int(input("Teclea las horas normales trabajadas:"))
    extras = int(input("Teclea las horas extras trabajadas:"))
    hora = int(input("Teclea el pago por hora:"))
    pagoNormal = calcularPagoNormal(normales, hora)
    pagoExtra = calcularPagoExtra(extras, hora)
    Total = pagoNormal + pagoExtra
    print("Pago normal: $%.2f" % pagoNormal)
    print("Pago extra: $%.2f" % pagoExtra)
    print("Pago total: $%.2f" % Total)


main()
