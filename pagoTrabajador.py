#encoding: UTF-8
#Autor: Alek Howland, A01747765
#Descripcion: Un programa que calcule el pago de un trabajador con un sueldo, horas y horas extras dadas.

def calcularPagoHora(horas, salario):   # Calcula el pago por hora
    pagoHora = salario * horas
    return pagoHora


def calcularPagoExtra(horasExtras, salario):    #Calcula pago de horas extras
    pagoExtra = (horasExtras * salario) * 1.85
    return pagoExtra


def calcularPagoTotal(pagoExtra, pagoHora): #Calcula el pago total
    pagoTotal = pagoExtra + pagoHora
    return pagoTotal


def imrpimir(pagoHora, pagoExtra, pagoTotal):   #Imprime los resultados
    print ("")
    print ("Pago normal: $%.2f" % (pagoHora))
    print ("Pago extra: $%.2f" % (pagoExtra))
    print ("-----------------------")
    print ("Pago total: $%.2f" % (pagoTotal))

def main(): #Función principal
    horas = int(input("Teclea las horas normales trabajadas : "))
    horasExtras = int(input("Teclea las horas extras trabajdas: "))
    salario = float(input("Teclea el pago por hora: "))
    calcularPagoHora(horas, salario)
    calcularPagoExtra(horasExtras, salario)
    calcularPagoTotal(calcularPagoHora(horas, salario), calcularPagoExtra(horasExtras, salario))
    imrpimir(calcularPagoHora(horas, salario),
             calcularPagoExtra(horasExtras, salario),
                calcularPagoTotal(calcularPagoHora(horas, salario), calcularPagoExtra(horasExtras, salario)))


main() #Se llama a la función principal


