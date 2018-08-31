# Autor: Erick David Ramírez Martínez, A01748155, Grupo: 2
# Descripción: Programa para calcular el pago de un trabajador de acuerdo a su sueldo por hora y las horas trabajadas

def pagoNormal(horasNormales,pagoPorHora):
    sueldoNormal = horasNormales*pagoPorHora

    return sueldoNormal


def pagoExtra(horasExtras,pagoPorHora):
    sueldoExtra = horasExtras*pagoPorHora*1.85

    return sueldoExtra


def main():
    horasNormales = float(input("Ingrese las horas normales trabajadas: "))
    horasExtras = float(input("Ingrese las horas extras trabajadas: "))
    pagoPorHora = float(input("Ingrese su sueldo por hora trabajada: "))

    pagoTotalNormal = pagoNormal(horasNormales,pagoPorHora)
    pagoTotalExtra = pagoExtra(horasExtras,pagoPorHora)

    pagoTotal = pagoTotalExtra+ pagoTotalNormal

# El print justo debajo de este comentario solo es para separar y dar un poco de formato y mejor visibilidad
    print("")
    print("Su pago normal es: $%0.2f"%(pagoTotalNormal))
    print("Su pago extra es: $%0.2f"%(pagoTotalExtra))
    print("-------------------------------------------------")
    print("Su pago total es: $%0.2f"%(pagoTotal))


main()
