# Autor: Alex Serrano Durán
# Este programa calcula el pago para un trabajador según las horas trabajadas


def calcularPago(horasNormales, salario):       # Calcula el pago normal
    pagoNormal = horasNormales * salario
    return pagoNormal


def calcularExtra(horasExtras, salario):        # Calcula el pago de horas extra
    pagoExtra = salario * 1.85 * horasExtras
    return pagoExtra


def main():          # Función main, pide el salario y las horas, suma el pago normal y el extra e imprime resultados
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    salario = int(input("Teclea el pago por hora: "))
    pagoNormal = calcularPago(horasNormales, salario)
    pagoExtra = calcularExtra(horasExtras, salario)
    pagoTotal = pagoNormal + pagoExtra
    print('''
Pago normal: $%.2f
Pago extra: $%.2f
-----------------------
Pago total: $%.2f''' % (pagoNormal, pagoExtra, pagoTotal))


main()
