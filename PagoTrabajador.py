# Autor: Luis Ricardo Chagala Cervantes
# Calcular el pago de un trabajador con horas extras incluidas


# La linea de codigo empieza después de esta linea

#Se calcula el precio de las horas normales de trabajo.
def CalcularpagoNormal(Normales, PagoHora):
    PagoNormal = Normales * PagoHora
    return PagoNormal

#Se calcula el precio de las horas extra de trabajo.
def CalcularpagoExtras(Extras, PagoHora):
    PagoExtra = Extras * ((PagoHora * 0.85) + PagoHora)
    return PagoExtra

#Se calcula el precio total de horas trabajadas.
def CalcularpagoTotal(Normales, Extras, PagoHora):
    PagoTotal = CalcularpagoNormal(Normales, PagoHora) + CalcularpagoExtras(Extras, PagoHora)
    return PagoTotal

def ImprimirResultado(PagoNormal, PagoExtra, PagoTotal):
    print("Pago Normal: %.2f" % (PagoNormal))
    print("Pago Extra: %.2f" % (PagoExtra))
    print("Pago Total: %.2f" % (PagoTotal))

def Imprimir(Normales, Extras, PagoHora):
    PagoNormal = CalcularpagoNormal(Normales, PagoHora)
    PagoExtra = CalcularpagoExtras(Extras, PagoHora)
    PagoTotal = CalcularpagoTotal(Normales, Extras, PagoHora)
    ImprimirResultado(PagoNormal, PagoExtra, PagoTotal)

def main():
   Normales = int(input("Horas normales trabajadas: "))
   Extras = int(input("Horas extras trabajadas: "))
   PagoHora = int(input("Pago por hora: "))
   Imprimir(Normales, Extras, PagoHora)

main()