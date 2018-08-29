# Author: Ivan Honc Ayón     A01376466       Grupo 2
# Descripción: Este programa calcula el pago total de un trabajador.


#Esta función multiplica el salario por las horas normales para calcular su salario en tiempo normal.
def pagoNormal(horasNormales, salario):
    pagoNorm = horasNormales*salario

    return pagoNorm


#Esta función multiplica el salario por las horas extra por el bonus de salario en tiempo extra para calcular el salario en tiempo extra.
def pagoExtra(horasExtra, salario):
    pagoExt = horasExtra*salario*1.85

    return pagoExt


#Esta es la función principal para recibir los valores del usuario y llamar al resto de las funciones.
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
