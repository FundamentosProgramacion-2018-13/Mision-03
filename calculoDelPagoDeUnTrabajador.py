#Autor: Alejandro Torices Oliva
#Es un programa que lee las horas normales y horas extra trabajadas en una semana
#e imprime el pago por cada una y el pago total.

#Calcula el pago para las horas normales.
def calcularPagoNormal(horasNormales, pagoPorHora):
    pagoNormal = horasNormales * pagoPorHora
    return pagoNormal

#Calcula el pago para las horas extras.
def calcularPagoExtra(horasExtras, pagoPorHora):
    pagoExtra = horasExtras * (pagoPorHora * 1.85)
    return pagoExtra

#Es la función principal, obtiene los datos e imprime las soluciones.
def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoPorHora = int(input("Teclea el pago por hora: "))
    pagoNormal = calcularPagoNormal(horasNormales, pagoPorHora)
    pagoExtra = calcularPagoExtra(horasExtras, pagoPorHora)
    pagoTotal = pagoNormal + pagoExtra
    print("""
Pago normal: $%.2f""" % pagoNormal)
    print("Pago extra: $%.2f" % pagoExtra)
    print("-----------------------")
    print("Pago total: $%.2f" % pagoTotal)


main()