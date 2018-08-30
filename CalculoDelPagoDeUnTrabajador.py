# Emiliano Heredia Garcia A01377072
# Calcula la paga de un empleado dado las horas trabajadas, las horas extras y el pago por hora.

def calcularNormal(horasNorm, pph):
    # Calcula la paga de las horas normales dada la cantidad de horas normales tabajadas por la paga por hora.
    return horasNorm*pph

def calcularExtra(horasExtr, pph):
    # Calcula la paga de las horas extras  dada la cantidad de horas extras tabajadas por la paga por hora.
    return horasExtr*(pph*1.85)

def pagoTtl(pagoNormal, pagoExtra):
    # Suma la cantidad de paga de horas normales y extras para calcular la paga total
    return pagoNormal+pagoExtra

def main():

    horasNorm = int(input("Teclea las horas normales trabajadas: "))
    horasExtr = int(input("Teclea las horas extras trabajadas: "))
    pph = int(input("Teclea el pago por hora: "))

    pagoNormal = calcularNormal(horasNorm, pph)
    pagoExtra = calcularExtra(horasExtr, pph)
    pagoTotal = pagoTtl(pagoNormal, pagoExtra)

    print("\nPago normal: %.2f" % pagoNormal)
    print("Pago extra: %.2f" % pagoExtra)
    print("-----------------------")
    print("Pago total: %.2f" % pagoTotal)

main()
