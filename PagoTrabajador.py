#Autor: Samantha MArtínez Franco
#Descripción: Calcular el pago semanal de un trabajador, con las horas trabajadas y las extras

def calcularHorasNormales (horasNormales, pagoHora):    #función que calcula el pago de las horas normales
    pagoHorasNormales=horasNormales*pagoHora
    return pagoHorasNormales

def calcularHorasExtras (horasExtras, pagoHora):     #función que calcula el pago de las horas extras
    pagoHorasExtra=horasExtras*1.85*pagoHora
    return pagoHorasExtra

def main():     #función principal
    horasNormales=int(input("Teclea las horas normales trabajadas: "))     #leer datos
    horasExtras=int(input("Teclea las horas extras trabajadas: "))
    pagoHora=int(input("Teclea el pago por hora: "))
    pagoHoraNormal=calcularHorasNormales(horasNormales,pagoHora)      #valor horas normales
    pagoHoraExtra=calcularHorasExtras(horasExtras,pagoHora)       #valor horas extras
    pagoTotal=calcularHorasNormales(horasNormales,pagoHora)+calcularHorasExtras(horasExtras,pagoHora)   #calculo pago total
    print("Pago normal: $%.2f" %(pagoHoraNormal))     #imprimir resultados
    print("Pago extra: $%.2f" % (pagoHoraExtra))
    print("------------------------")
    print("Pago total: $%.2f" % (pagoTotal))


#llamar función principal
main()
