#Autor Claudio Mayoral García
#Descripción: Pide las horas trabajadas de un trabajador a la semana (Horas normales y horas extra) y el salario por hora del mismo
# y entrega el pago semanal


def calcularPagoExtra(horasExtras, pagoPorHora):
    #Calcula el pago de las horas extras multiplicando las horas por el salario por hora
    #Regresa pagoExtra
    pagoExtra = horasExtras * pagoPorHora * 1.85
    return pagoExtra


def calcularPagoNormal(horasNormales, pagoPorHora):
    #Calcula el pago con las horas normales multiplicando las horas por el salario por hora
    #Regresa pagoNormal
    pagoNormal = horasNormales * pagoPorHora
    return pagoNormal


def main():
    # horasNormales = Lee las horas normales trabajadas
    # horasExtras = Lee las horas extras trabajadas
    # pagoPorHora = Lee el pago por hora del trabajador
    # Calcula pagoNormal y PagoExtra por las funciones calcularPagoNormal y calcularPagoExtra
    # Calcula pagoTotal sumando PagoExtra y PagoNormal
    # Imprime un espacio en blanco, pagoNormal, pagoExtra, guiones y el pagoTotal
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoPorHora = float(input("Teclea el pago por hora: "))
    pagoNormal = calcularPagoNormal(horasNormales, pagoPorHora)
    pagoExtra = calcularPagoExtra(horasExtras, pagoPorHora)
    pagoTotal = pagoNormal + pagoExtra
    print("")
    print("Pago normal: $%.2f" % pagoNormal)
    print("Pago extra: $%.2f" % pagoExtra)
    print("-----------------------")
    print("Pago total: $%.2f" % pagoTotal)



