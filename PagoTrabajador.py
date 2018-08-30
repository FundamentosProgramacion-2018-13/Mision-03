# Autor: Luis Humberto Burgueño Paz
# Calcula el pago normal, el pago extra y el pago total de un trabajador

# Recibe como parámetros las horas normales y el pago por hora y regresa el pago normal total
def calcularPagoNormal(horasNormales, pagoPorHora):
   pagoNormal = horasNormales * pagoPorHora
   return pagoNormal

# Recibe como parámetros las horas extras y el pago por hora para calcular el pago extra
def calcularPagoExtra(horasExtras, pagoPorHora):
   pagoExtra = (horasExtras*pagoPorHora) * 1.85
   return pagoExtra

# Lee las horas normales, horas extra y el pago por hora e imprime el pago normal, el pago extra y el pago total
def main():
   horasNormales = int(input("Teclea las horas normales trabajadas: "))
   horasExtras = int(input("Teclea las horas extras trabajadas: "))
   pagoPorHora = int(input("Teclea el pago por hora: "))
   pagoNormal = calcularPagoNormal(horasNormales, pagoPorHora)
   pagoExtra = calcularPagoExtra(horasExtras, pagoPorHora)
   pagoTotal = pagoNormal + pagoExtra
   print("Pago Normal: $%.02f" % pagoNormal)
   print("Pago Extra: $%.02f" % pagoExtra)
   print("-----------------------")
   print("Pago Total: $%.02f" % pagoTotal)


main()
