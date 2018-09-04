#Joshua Sánchez Martínez A01274269
#Pedide al usuario sus horas de trabajo para calcular su salario

def calcularPagoNormal(horasH,pagoPH):

    pagoNormal = horasH * pagoPH

    return pagoNormal


def calcularPagoExtra (horasE,pagoPH):

    pagoExtra = ( ((85*pagoPH)/100) *horasE )+ (horasE*pagoPH)

    return pagoExtra

def main():

    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extra trabajadas: "))
    pagoPorHora = float(input("Teclea el pago por hora: $"))

    pagoNormal = calcularPagoNormal(horasNormales, pagoPorHora)
    pagoExtra = calcularPagoExtra(horasExtras, pagoPorHora)

    pagoTotal = pagoNormal + pagoExtra

    print("El pago normal es: $ %.2f" % pagoNormal)
    print("El pago extra es: $ %.2f" % pagoExtra)
    print("El pago total es: $ %.2f" % pagoTotal)

main()