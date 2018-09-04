# Autor: Jesús Emmanuel Alcalá Nava
# Descripción: calcula el pago a un trabajador dependiendo de las horas que trabaja
def calcularPago(horasNormales, salario):
    pagoNormal = horasNormales * salario #Calcula el pago de horas normales
    return pagoNormal
def calcularExtra(horasExtras, salario):
    pagoExtra = salario * 1.85 * horasExtras #Calcula el pago de hora extras
    return pagoExtra
def main():
    horasNormales = int(input("Horas normales trabajadas: ")) #Pide al usuario la cantidad de horas
    horasExtras = int(input("Horas extras trabajadas: "))
    salario = int(input("Pago por hora: "))
    pagoNormal = calcularPago(horasNormales, salario)
    pagoExtra = calcularExtra(horasExtras, salario)
    pagoTotal = pagoNormal + pagoExtra
    print("Pago normal: $%.2f Pago extra: $%.2f Pago total: $%.2f" % (pagoNormal, pagoExtra, pagoTotal))
main()