#Jocelyn López Ortíz A01377451
#Cálculo del pago semanal de un trabajador

def calcularPagoNormal(horasNormales, pagoPorHora):
    pagoNormal = horasNormales*pagoPorHora
    return pagoNormal

def calcularPagoExtra(horasExtras, pagoPorHora):
    pagoExtra = horasExtras*pagoPorHora + horasExtras*pagoPorHora*0.85
    return pagoExtra

def main():
    pagoN = int(input("Teclea las horas normales trabajadas: "))
    pagoE = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))
    pagoNormal = calcularPagoNormal(pagoN, pagoHora)
    pagoExtra = calcularPagoExtra(pagoE, pagoHora)
    print()
    print("Pago normal: $%.2f" %(pagoNormal))
    print("Pago extra: $%.2f" % (pagoExtra))
    print("--------------------------")
    print("Pago total: $%.2f" %(pagoNormal+pagoExtra))

main()
