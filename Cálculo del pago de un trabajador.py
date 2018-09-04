#Autor: Carlos Alberto Reyes Ortiz
#Pago de un trabajador


def calcularPagoNormal(horasNormales, pagoPorHora):   #Calcula el pago normal
    pagoNormal = horasNormales * pagoPorHora
    return pagoNormal


def calcularPagoExtra(horasExtras, pagoPorHora):        #Calcula el pago extra
    pagoExtra =  ( 1.85 * pagoPorHora ) * horasExtras
    return pagoExtra



def main(): #Función principal: te da tu pago normal, extra y total
    horasNormlaes = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoPorHora = int(input("Teclea el pago por hora: "))
    print()
    pagoNormal = calcularPagoNormal(horasNormlaes, pagoPorHora)
    pagoExtra = calcularPagoExtra(horasExtras, pagoPorHora)
    pagoTotal = pagoExtra + pagoNormal
    print("Pago normal: $%.2f" %(pagoNormal))
    print("Pago extra: $%.2f" % (pagoExtra))
    print("-----------------------") #Son 23 exctas, como el ejemplo del profe
    print("Pago total: $%.2f" % (pagoTotal))


main()

