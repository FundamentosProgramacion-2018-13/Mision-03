# Author: Ivan Honc Ayón     A01376466       Grupo 2
# Descripción: Este programa calcula el pago total de un trabajador.


def pagoNormal(horasNormales, salario):
    pagoNorm = horasNormales*salario

    return pagoNorm


def pagoExtra(horasExtra, salario):
    pagoExt = horasExtra*salario*1.85

    return pagoExt


def main():
    normal = float(input("Teclea las horas normales trabajadas: "))
    extra = float(input("Teclea las horas extra trabajadas: "))
    sal = float(input("Teclea el pago por hora: "))
    norm = pagoNormal(normal, sal)
    ext = pagoExtra(extra, sal)
    total = norm + ext

    print("""
Pago normal: $%.2f""" % norm)
    print("Pago extra: $%.2f" % ext)
    print("-----------------------")
    print("Pago total: $%.2f" % total)


main()
