# Autor: Juan Carlos Flores García, A01376511

# Descripción: Programa que imprime los datos de un trabajador y calcula su pago semanal.


# La siguiente función calcula el pago normal del trabajador.
def calcularPagoNormal(horasNormales, pagoPorHora):
    pagoNormal = pagoPorHora * horasNormales
    return pagoNormal


# La siguiente función calcula el pago extra del trabajador.
def calcularPagoExtra(horasExtras, pagoPorHora):
    pagoExtra = (horasExtras * pagoPorHora) * 1.85
    return pagoExtra


# La siguiente función imprime el pago normal, el pago extra y el pago total del trabajador.
def imprimir(pagoNormal, pagoExtra, pagoTotal):
    print("Pago normal: $%.2f" % pagoNormal)
    print("Pago extra: $%.2f" % pagoExtra)
    print("-----------------------")
    print("Pago total: $%.2f" % pagoTotal)


# La función principal lee el valor de las horas normales, las horas extra y el pago por hora.
# También calcula el pago normal, el pago extra, el pago total y los imprime usando sus respectivas funciones.
def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoPorHora = float(input("Teclea el pago por hora: "))
    pagoNormal = calcularPagoNormal(horasNormales, pagoPorHora)
    pagoExtra = calcularPagoExtra(horasExtras, pagoPorHora)
    pagoTotal = pagoNormal + pagoExtra
    imprimir(pagoNormal, pagoExtra, pagoTotal)


# Llama a la función main.
main()

