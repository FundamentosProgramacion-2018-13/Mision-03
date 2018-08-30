# encoding: UTF-8
# Autor: Diego Palmerin Bonada, A01747290
# Descripcion: Calcula el suelo semanal de un trabajador tomando sus horas normales y extras

"""
Análisis
E: horasNormales, horasExtra, pagoPorHora
S: Sueldo
E/S:
sueldoNormal=horasNormales*pagoPorHora
sueldoExtra=horasExtra*pagoPorHora*1.85
sueldoTotal=sueldoNormal+sueldoExtra

Algoritmo:
Preguntar al usuario horas normales trabajadas, horas extra trabajadas y el pago que se da por hora
Llamar función horas normales dando como varialbes horas normales y pago por hora
Multiplicar horas normales por su pago por hora y regresarlo a main para que lo imprima
Llamar función horas extra dando como varuables horas extra y pago por hora
Multiplicar horas extra por su pago por hora y el producto por 1.85.
Regresarlo a main para que lo imprima
Llamar función sumaTotal con las variables de sueldo normal y sueldo extra
Sumar los dos datos y regresarlo a main para que lo imprima
"""

def sueldoNormal(horas, sueldo):
    return(horas*sueldo)


def sueldoExtra(horas, sueldo):
    return(horas*sueldo*1.85)


def sumarSueldos(normal,extra, sueldo):
    sueldoNormal(normal, sueldo)
    sueldoExtra(extra, sueldo)
    return(sueldoNormal+sueldoExtra)


def main():
    horasNormal = int(input("Teclea las horas normales trabajadas: "))
    horasExtra = int(input("Teclea las horas extras trabajadas: "))
    pagoPorHora = float(input("Teclea el pago por hora: "))
    print("Pago normal: $%.2f" % (sueldoNormal(horasNormal,pagoPorHora)))
    print("Pago extra: $%.2f" % (sueldoExtra(horasExtra, pagoPorHora)))
    print("------------------------")
    print("Pago total: $%.2f" % (sumarSueldos(horasNormal, horasExtra, pagoPorHora)))


main()