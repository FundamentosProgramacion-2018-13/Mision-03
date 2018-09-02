# Autor: Rubén Villalpando Bremont
# Programa que calcula el pago total de un trabajador tomando en cuenta las horas extras.

# Esta funcion calcula el pago por las horas normales trabajadas
def calculoPagoNormal(horasNormalesTrabajadas, dineroPorHora):
    pagoNormal = horasNormalesTrabajadas*dineroPorHora
    return pagoNormal

# Función que calcula el pago por las horas extras trabajadas
def calculoPagoExtra(horasExtrasTrabajadas, dineroPorHora):
    pagoExtra = horasExtrasTrabajadas*dineroPorHora*1.85
    return pagoExtra


# Función main
def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoPorHora = int(input("Teclea el pago pot hora: "))
    pagoNormal = calculoPagoNormal(horasNormales, pagoPorHora)
    pagoExtra = calculoPagoExtra(horasExtras, pagoPorHora)
    pagoTotal = pagoNormal + pagoExtra
    print("Pago normal: $%.2f" % (pagoNormal))
    print("Pago Extra: $%.2f" % (pagoExtra))
    print("------------------------")
    print("Pago total: $%.2f" % (pagoTotal))

# Llamar a main
main()