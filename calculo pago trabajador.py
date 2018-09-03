# JavierAlexandro Vargas Sánchez A01377718
'''Programa que calcula el pago por horas normales, el pago por horas extras, y suma estos dos para calcular el
pago total que recibira el trabajador'''


def calcularPagoNormal(horasNormales, pagoPorHora):   #calcula lo que gana el trabajador por sus horas de trabajo normales
    pagoNormal = horasNormales * pagoPorHora
    return pagoNormal


def calcularPagoExtra(horasExtra, pagoPorHora):  # calcula lo que gana el trabajador, por sus horas extra de trabajo
    pagoExtra = (pagoPorHora * 1.85) * horasExtra
    return pagoExtra


def calcularPagoTotal(pagoNormal, pagoExtra): # Suma las ganancias, obteniendo el pago total
    pagoTotal = pagoNormal + pagoExtra
    return pagoTotal


def imprimir(pagoNormal, pagoExtra, pagoTotal): #Imprime el pago por horas normales, extras y el pago total
    print()
    print("Pago normal: $",format(pagoNormal, ".2f"))
    print("Pago extra: $", format(pagoExtra, ".2f"))
    print("-----------------------")
    print("Pago Total: $", format(pagoTotal, ".2f"))


def main():
    horasNormales = int(input("Teclea la horas normales trabajadas: "))
    horasExtra = int(input("Teclea las horas extras trabajadas: "))
    pagoPorHora = int(input("Teclea el pago por hora: "))
    pagoNormal = calcularPagoNormal(horasNormales, pagoPorHora)
    pagoExtra = calcularPagoExtra (horasExtra, pagoPorHora)
    pagoTotal = calcularPagoTotal(pagoNormal, pagoExtra)
    imprimir (pagoNormal, pagoExtra, pagoTotal)



main()