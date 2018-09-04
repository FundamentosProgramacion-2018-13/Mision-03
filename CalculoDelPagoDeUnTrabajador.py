# Autor: Luis Armando Miranda Alcocer
# Calcula el pago normal y el de horas extras de un trabajador, si se paga por hora, y las horas extras se pagan 85% más

def calcularPagoNormal (horasNormales, horasExtra, pagoPorHora):
    pagoNormal = horasNormales * pagoPorHora #Se calcula el pago por las horas trabajadas
    return pagoNormal

def calcularPagoExtra(horasNormales, horasExtra, pagoPorHora):
    pagoExtra = horasExtra* pagoPorHora*1.85 #Se calcula el pago de las horas extra, se multiplica 1.85 para sacar el 85 porciento de más de las horas normales.
    return pagoExtra

def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))  #Leer horas de trabajo normal, extra, y pago por hora
    horasExtra = int(input("Teclea las horas extras trabajadas: "))
    pagoPorHora = int(input("Teclea el pago por hora: "))
    pagoNormal = calcularPagoNormal(horasNormales, horasExtra, pagoPorHora)  #Llamar funciones
    pagoExtra = calcularPagoExtra(horasNormales, horasExtra, pagoPorHora)
    print ( )
    print ("Pago normal: %.2f" %(pagoNormal)) #Con dos decimales
    print ("Pago extra: %.2f" %(pagoExtra))
    print ("----------------------")
    print ("Pago total: %.2f" %(pagoNormal+pagoExtra))  #Suma del total

main()
