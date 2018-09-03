#Damián Iván García Ravelo
#A01376354
#Programa que calcula el pago que recibe un trabajador

def calcularPagoHoraNormal (horasNormales, precioPorHora):
#Calcula el pago que se hace por horas normales
    pagoPorHoraNormal = horasNormales * precioPorHora
    return pagoPorHoraNormal

def calcularPagoHoraExtra (horasExtras, precioPorHora):
#Calcula el pago que se hace por horas extras
    pagoPorHoraExtra = horasExtras * (precioPorHora * 1.85) #Multiplica a las horas extras por el 85% más del pago por hora
    return pagoPorHoraExtra

def main ():
#Pregunta al usuario las horas normales, extras y el pago por hora normal
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    precioPorHora = int(input("Teclea el pago por hora: "))
#Asigna las variables de la función
    pagoPorHoraExtra = calcularPagoHoraExtra(horasExtras, precioPorHora)
    pagoPorHoraNormal = calcularPagoHoraNormal (horasNormales, precioPorHora)
    pagoTotal = pagoPorHoraExtra + pagoPorHoraNormal #Calcula el pago Total
#Imprime el pago normal, el pago extra y la suma de los dos

    print ("Pago normal: $ ", format(pagoPorHoraNormal, ".2f"))
    print("Pago extra: $ ", format(pagoPorHoraExtra, ".2f"))
    print ("-----------------------")
    print("Pago total: & ", format(pagoTotal, ".2f"))

main () #Lllama a la función