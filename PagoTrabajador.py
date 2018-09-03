# Autor: Jonathan Sanabria Rocha
# Calcular el pago semanal de un trabajador

def calcularPagonormal(horasnormales,pagohora):
    pagonormal = horasnormales*pagohora
    return pagonormal
#Calcula el pago de la horas normales de trabajo.

def calcularPagoextra(horasextra,pagohora):
    pagohoraextra = pagohora*0.85
    pagoextra = horasextra*(pagohora+pagohoraextra)
    return pagoextra
#Calcula el pago de la horas extras trabajadas.

def calcularPagototal(pagonormal,pagoextra):
    pagototal = pagonormal+pagoextra
    return pagototal
 #Calcula el pago total o semanal que involucra el pago de horas normales con horas extra.

def main():
    horasnormales = int(input("Teclea las horas normales trabajadas: "))
    horasextra = int(input("Teclea las horas extra trabajadas: "))
    pagohora = int(input("Teclea el pago por hora: "))
    pagonormal = calcularPagonormal(horasnormales,pagohora)
    pagoextra = calcularPagoextra(horasextra,pagohora)
    pagototal = calcularPagototal(pagonormal,pagoextra)

    print("Pago normal: $%.2f" % pagonormal)
    print("Pago extra: $%.2f" % pagoextra)
    print("------------------------------------")
    print("Pago total: $%.2f" % pagototal)

main()




