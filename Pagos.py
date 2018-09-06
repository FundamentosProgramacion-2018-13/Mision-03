# Alex Fernando Leyva Martinez / A01747078
# Calcular el Pago Normal, Pago por horas Extra y Pago Semanal

#Permite calcular el pago por horas normales
def pagoNormal(horasNormales,pagoHora):
    horasNormal = (horasNormales * pagoHora)
    return horasNormal

#Permite calcular el pago por horas extras
def pagoExtra(horasExtras,pagoHora):
    horasExtra = (horasExtras*pagoHora)*1.85
    return horasExtra

#Pregunta los datos y llama a las funciones anteriores
def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea al pago por hora: "))
    print("   ")
    horasNormal = pagoNormal(horasNormales,pagoHora)
    horasExtra = pagoExtra(horasExtras,pagoHora)
    print("Pago Normal: $%.2f" % horasNormal)
    print("Pago Extra: $%.2f" % horasExtra)
    print("----------------------")
    pagoTotal = horasExtra + horasNormal
    print("Pago Total: $%.2f" % pagoTotal)

main()
