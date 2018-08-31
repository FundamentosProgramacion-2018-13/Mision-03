# Autor: Zabdiel Valentin Garduño Vivanco, A01377950
# Descripcion: Sacar el pago normal y de horas extra.


def pagoNormal(horas, pago):
    pagoNormal=horas*pago
    return pagoNormal

def pagoExtra(horas, pago):
    pagoExtra=horas*pago
    bonus=pagoExtra*0.85
    pagoExtra=pagoExtra+bonus
    return pagoExtra

def main():
    horasNormales=int(input("Teclea las horas normales trabajadas: "))
    horasExtras=int(input("Teclea las horas extras trabajadas: "))
    pagoHora=int(input("Teclea el pago por hora: "))

    pagoN=pagoNormal(horasNormales,pagoHora)
    pagoExt=pagoExtra(horasExtras, pagoHora)

    print("pago normal: %.2f" %(pagoN))
    print("pago extra: %.2f" %(pagoExt))

    pagoTotal=pagoN+pagoExt

    print("----------------")

    print("pago total: %.2f" %(pagoTotal))

main()






