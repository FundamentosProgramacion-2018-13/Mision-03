# Autor: Oscar Alejandro Torres Maya, A01377686, grupo 04
# Descripción: Programa que calcula el pago normal por hora y por horas extras, además sumar las extra con las normales

#Funcion para calcular el pago normal por hora
def pagoNormal(horasNormales, pagoHora):
    normalesTrabajadas = horasNormales*pagoHora
    return normalesTrabajadas

#Funcion para calcular el pago por horas extras
def pagoExtra(horasExtras, pagoHora):
    extrasTrabajadas = ((horasExtras*0.85)+horasExtras)*pagoHora
    return extrasTrabajadas

# Función principal, lee datos e imprime datos. Además de calcular el total de pago
def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = float(input("Teclea el pago por hora: "))
    normal = pagoNormal(horasNormales, pagoHora)
    extra = pagoExtra(horasExtras, pagoHora)
    pagoTotal = normal + extra

    print("")
    print("Pago normal: $%0.2f" % (normal))
    print("Pago extra: $%0.2f" % (extra))
    print("-----------------------")
    print("Pago total: $%0.2f" % (pagoTotal))

main()