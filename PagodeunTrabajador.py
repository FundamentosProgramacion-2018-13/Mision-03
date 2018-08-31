#Autor: Jesus Zabdiel Sanchez Chavez A01374964

#Descripcion:Calcula el pago total de un atrabajador, así como el pago normal y el pago extra, con base
# en sus horas trabajadas y el pago por dia.

#funcion principal
def main ():
    horas = int (input("Teclea las horas normales trabajadas: "))
    horasextras = int (input("Teclea las horas extras trabajadas: "))
    pago = int (input("Tecle el pago por hora: "))
    pagoNormal = calcularPagoNormal(horas, pago)
    pagoExtra = calcularPagoExtra(horasextras, pago)
    pagoTotal = pagoExtra + pagoNormal
    print ('''    Pago normal: $%.2f
    Pago extra: $%.2f
    -------------------
    Pago total: $%.2f   ''' % (pagoNormal, pagoExtra,pagoTotal ))

#calcula el pago por las horas normales trabajadas
def calcularPagoNormal(horas, pago):
    pagoNormal = horas * pago
    return pagoNormal
# calcula el pago por las horas extras
def calcularPagoExtra(horasextras, pago):
    pagoExtra = (horasextras * (pago*.85)) + horasextras * pago
    return pagoExtra

main()