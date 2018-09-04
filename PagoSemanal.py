#Autor: Daniel Cordova Bermudez
#Descripción: En este programa calcula el pago de un trabajador semanalmente

def calcularPagoNormal(horasN, pagoHora):
    pagoNormal = pagoHora*horasN
    return pagoNormal

def calcularPagoExtra(horasE, pagoHora):
    pagoNormal = pagoHora*horasE
    pagoExtra = pagoHora*horasE*0.85
    pagoExtra = pagoExtra + pagoNormal
    return pagoExtra

def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtra = int(input("Teclea las horas extras trabajadas: "))
    pagoPorhora = int(input("Teclea el pago por hora: "))

    pagoNormal = calcularPagoNormal(horasNormales, pagoPorhora)
    pagoExtra = calcularPagoExtra(horasExtra, pagoPorhora)
    pagoTotal = pagoNormal + pagoExtra
    print("""
Pago normal: $%.2f 
Pago extra: $%.2f
-------------------
Pago total: $%.2f """ % (pagoNormal,pagoExtra,pagoTotal))

main()
