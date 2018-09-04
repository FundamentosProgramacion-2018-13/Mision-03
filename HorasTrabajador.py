# Autor: Dvid Isaí López Jaimes
# Calcula el pago normal, pago total y pago estra de un trabajador

def pagoNormal(horasNormal, pagoHora):
    pagoNorm = horasNormal * pagoHora
    return pagoNorm

def pagoextra (horasExtra, pagoHora):
    pagoext = pagoHora * 0.85
    pagoext = pagoext + pagoHora
    pagoext = pagoext * horasExtra
    return pagoext

def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoHrs = int(input("Teclea el pago por hora: "))

    totalNormal = pagoNormal(horasNormales, pagoHrs)
    print("Pago normal: $",format(totalNormal, ".2f"))

    totalExtra = pagoextra(horasExtras, pagoHrs)
    print("Pago extra: $",format(totalExtra, ".2f"))

    pagoTotal = totalNormal + totalExtra
    print("Pago total: $",format(pagoTotal, ".2f"))


main()