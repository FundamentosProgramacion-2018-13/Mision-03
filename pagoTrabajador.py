#Autor: Víctor Manuel Rodríguez Loyola A01747755
#Descripción: Este programa calcula el pago semanal de un trabajador.


def calcularPagoNormal(hrsNormales, pagoHora): #Calcula el pago correspondiente a las horas normales trabajadas
    pagoNormal= hrsNormales * pagoHora
    return pagoNormal


def calcularPagoExtra(hrsExtra, pagoHora): #Calcula el pago correspondiente a las horas extras trabajadas
    pagoExtra = hrsExtra*(pagoHora*1.85)
    return pagoExtra

def main():
    horasNormales= int(input("Teclea las horas normales trabajadas: "))
    horasExtra = int(input("Teclea las horas extras trabajadas: "))
    pagoPorHora= int(input("Teclea el pago por hora: "))
    pagoNormal= calcularPagoNormal (horasNormales, pagoPorHora)
    pagoExtra = calcularPagoExtra (horasExtra, pagoPorHora)
    pagoTotal= pagoExtra+pagoNormal
    print("Pago normal: $%.2f" % (pagoNormal))
    print("Pago extra: $%.2f" %(pagoExtra))
    print("------------------------")
    print("Pago total: $%.2f" %(pagoTotal))


main()
