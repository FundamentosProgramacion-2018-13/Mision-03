#Autor;Diana Marisol Medina Bravo
#Lee las horas normales, las horas extras y el pago por hora de un trabajador y se cálcula e imprime el pago normal,
#el pago extra y el pago total

#Función para calcular el pago normal
#Recibe las horas normales y el pago por hora dy regresa el pago normal
def calcularPagoNormal(horasNormales,pagoPorHora):
    pagoNormal= horasNormales*pagoPorHora
    return pagoNormal

#Función para calcular el pago extra
#Recibe las horas extras y el pago por hora de un trabajador y regresa el pago extra
def calcularPagoExtra(horasExtras,pagoPorHora):
    pagoExtra=pagoPorHora*1.85*horasExtras
    return pagoExtra

#Función principal resuelve el problema
def main():
    horasNormales=(int(input("Teclea las horas normales trabajadas: ")))
    horasExtras=(int(input("Teclea las horas extras trabajadas: ")))
    pagoPorHora=(int(input("Teclea el pago por hora: ")))
    pagoNormal= calcularPagoNormal(horasNormales,pagoPorHora)
    pagoExtra= calcularPagoExtra(horasExtras,pagoPorHora)
    pagoTotal=pagoNormal+pagoExtra
    print("")
    print("Pago normal: $%.2f" % pagoNormal)
    print("Pago extra: $%.2f" % pagoExtra)
    print('-------------------------')
    print("Pago total: $%.2f" % pagoTotal)

#Llama a la función
main()