# Autor: Oscar Macias Rodríguez
# Descripción: Calcula e imprime los datos del trabajador incluyendo su pago semanal.

# Calcula el pago normal.
def pagoNormal(horasNormales, pagoXhora):
    pagoNormal = horasNormales * pagoXhora
    return pagoNormal

# Calcula el pago extra.
def pagoExtra(horasExtras, pagoXhora):
    p = horasExtras * pagoXhora
    p1 = p * 0.85
    pagoExtra = p + p1
    return pagoExtra

# Imprime en pantalla el pago normal, el pago extra y el pago total.
def main():
    horasNormales = int(input("Teclea las horas normales trabajadas:"))
    horasExtras = int(input("Teclea las horas extras trabajadas:"))
    pagoXhora = int(input("Teclea el pago por hora:"))

    pagoNormal(horasNormales, pagoXhora)
    pagoExtra(horasExtras, pagoXhora)
    pagoTotal = pagoNormal(horasNormales, pagoXhora) + pagoExtra(horasExtras, pagoXhora)

    print("")
    print("Pago normal:", "$%0.2f" % pagoNormal(horasNormales, pagoXhora))
    print("Pago extra:", "$%0.2f" % pagoExtra(horasExtras, pagoXhora))
    print("-----------------------")
    print("Pago total:", "$%0.2f" % pagoTotal)


main()