#irma Gómez carmona
#Calcular el pago que recibirá un trabajador por sus horas de jornada más sus horas extra


def calcularPagoHN(hNoramles, sueldo):  #HN=horas normales
    pagoHN= hNoramles*sueldo
    return pagoHN
def calcularPagoHE (hExtras, sueldo):
    pagoHE= sueldo*1.85*hExtras
    return pagoHE

def main ():
    horasN=int(input("Teclea las horas normales trabajadas: "))
    horasE = int(input("Teclea las horas extras trabajadas: "))
    pagoxhora = int(input("Teclea el pago por hora: "))
    NumHNormales = calcularPagoHN(horasN,pagoxhora)
    NumhExtras = calcularPagoHE(horasE,pagoxhora)
    total = NumhExtras+NumHNormales
    print("""
    Pago normal: $ %.2F
    Pago extra: $ %.2f
    ---------------------
    Pago total: $ %.2f""" % (NumHNormales,NumhExtras,total))

main ()
