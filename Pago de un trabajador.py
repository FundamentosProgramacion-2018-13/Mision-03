# Autor: Humberto Carrillo Gómez
"""Descripción: Este programa calcula el pago semanal, el pago extra y el pago total de un trabajador utilizando
funciones"""

# Recibe horas normales y pago y los utiliza para calcular el pago normal.
def calcularPagoNormal(horasN, pago):
    pagoNormal=horasN*pago
    return pagoNormal

# Recibe horas extra y pago para calcular el pago extra.
def calcularPagoExtra(horasE, pago):
    pagoExtra= horasE*(185*pago)/100
    return pagoExtra

# Recibe pago normal y pago extra para calcular el pago total.
def calcularPagoTotal(pagoExtra, pagoNormal):
    pagoTotal= pagoNormal+pagoExtra
    return pagoTotal

# Función principal, incorpora a las funciones anteriormente creadas para resolver el problema e impreme las salidas.

def main():
    horasN=int(input("Teclea las horas normales trabajadas: "))
    horasE=int(input("Teclea las horas extra trabajadas: "))
    pago=int(input("Teclea el pago por hora: "))
    pagoNormal=calcularPagoNormal(horasN,pago)
    pagoExtra=calcularPagoExtra(horasE,pago)
    pagoTotal=calcularPagoTotal(pagoExtra,pagoNormal)
    print()
    print("Pago Normal: $%.2f" % pagoNormal)
    print("Pago Extra: $%.2f" % pagoExtra)
    print("""-----------------------
Pago Total: $%.2f"""% pagoTotal)

#LLamar a la función principal
main()