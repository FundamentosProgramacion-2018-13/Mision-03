# Autor: Zoe Caballero Dominguez Matrícula: A01747247
"""Descripción: El programa pide las horas normales y extras trabajadas, junto el pago por hora.
Calcula el pago por las horas y el pago total."""

# Programa

"""Función calcularPagoNormal hace la operación correspondiente para sacar el pago 
de las horas normales y lo regresa a main"""
def calcularPagoNormal(horasNormales, pagoHora):
    pagoHoraNormal = horasNormales * pagoHora
    return pagoHoraNormal


# Función calcularPagoExtra hace la operación correspondiente para sacar el pago por las joras extra y lo regresa a main
def calcularPagoExtra(horasExtra, pagoHora):
    pagoHoraExtra = horasExtra * (pagoHora * 1.85)
    return pagoHoraExtra


# La función main pide las horas trabajadas y el pago por hora.
# Y llama a otras funciones para calcular el pago, calcula el total e imprime los resultados.
def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtra = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))
    pagoNormal = calcularPagoNormal (horasNormales, pagoHora)
    pagoExtra = calcularPagoExtra (horasExtra, pagoHora)
    pagoTotal = pagoNormal + pagoExtra
    print("Pago normal: $%.2f" % (pagoNormal))
    print("Pago extra: $%.2f" % (pagoExtra))
    print("-----------------------")
    print("Pago total: $%.2f" % (pagoTotal))

#Llamar a la función main
main()