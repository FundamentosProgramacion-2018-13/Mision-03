# Carlos Badillo García             A01377618
# Programa que lee las horas normales, las horas extras y el pago de un trabajador; también calcula e imprime los datos del trabajador incluyendo su pago semanal

def calcularPagoNormal(horasNormales, pagoHora):    #Función que sirve para obtener cuanto gana del pago normal
    pagoNormal = pagoHora * horasNormales
    return pagoNormal

def calcularPagoExtra(horasExtras, pagoHora):   #Función que sirve para obtener cuanto gana del pago extra
    pagoExtra = (horasExtras * pagoHora) * 1.85
    return pagoExtra

def main(): #Función que sirve para que el usuario introdusca las horas normales, las horas extras y el pago por hora. imprime cuanto vale el pago normal, el pago extra y calcula e imprime el pago total.
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))
    print()
    pagoNormal = print("Pago normal: $%.2f" %calcularPagoNormal(horasNormales, pagoHora))
    pagoExtra = print("Pago extra: $%.2f" %calcularPagoExtra(horasExtras, pagoHora))
    print("-----------------------")
    total = calcularPagoNormal(horasNormales, pagoHora) + calcularPagoExtra(horasExtras, pagoHora)
    pagoTotal = print("Pago total: $", format(total, ".2f"))

main()