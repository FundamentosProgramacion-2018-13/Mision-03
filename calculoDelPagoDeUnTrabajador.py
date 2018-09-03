#Autor: Michelle Sánchez Guerrero
#Descripción: Programa que calcula el pago de un trabajador.

#Función que calcula el pago por las horas normales trabajadas.
def calcularPagoNormal(horasNormales, pagoHora):
    pagoNormal = horasNormales * pagoHora
    return pagoNormal

#Función que calcula el pago por las horas extras trabajadas.
def calcularPagoExtra(horasExtras, pagoHora):
    pagoExtra = horasExtras * (pagoHora * 1.85)
    return pagoExtra

#Función principal. Lee datos e imprime resultados
def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))
    pagoNormal = calcularPagoNormal(horasNormales, pagoHora)
    pagoExtra = calcularPagoExtra(horasExtras, pagoHora)
    pagoTotal = pagoNormal + pagoExtra
    print()
    print("Pago normal: $%.02f" % (pagoNormal))
    print("Pago extra: $%.02f" % (pagoExtra))
    print("-----------------------")
    print("Pago total: $%.02f" % (pagoTotal))

#Llamar a la función principal
main()