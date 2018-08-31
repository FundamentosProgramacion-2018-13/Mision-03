"""
Nombre: Alexys Martín Coate Reyes
Martícula: A01746998

Descripción: Calcular el pago semanal de un trabajador, contando su número de horas extras.
"""

#Calcula el pago de horas normales con base el el pago por hora
def calcularPagoN(horasT, pagoH):
    pagoN = horasT * pagoH
    return pagoN

#Calcula el pago de horas extras con base a un incremento de sueldo del %85
def calcularPagoE(horasE, pagoH):
    pagoE = horasE * (pagoH*1.85)
    return pagoE

#Calcula el total a pagar
def calcularTotal(pagoN, pagoE):
    total = pagoN + pagoE
    return total

#Imprime las horas de trabajo, extras, así como el cálculo de los pagos y el total de los mismos
def imprimir(horasT, horasE, pagoN, pagoE, total):
    print("""Horas Trabajadas: %d
Horas Extras: %d
        Pago normal: $%.2f
        Pago extra: $%.2f
        Pago total: $%.2f""" % (horasT, horasE, pagoN, pagoE, total))

#Función principal que engloba toda la serie de pasos para resolver el resultado. También obtiene los datos de entrada.
def main():
    horasT = int(input("Horas trabajadas: "))
    horasE = int(input("Horas extras: "))
    pagoH = float(input("Pago por hora: "))
    pagoN = calcularPagoN(horasT, pagoH)
    pagoE = calcularPagoE(horasE, pagoH)
    total = calcularTotal(pagoN, pagoE)
    imprimir(horasT, horasE, pagoN, pagoE, total)

#Llama a la función principal para que se ejecute
main()