#Autor: Alberto Contreras Torres
#Calcula el pago por horas de trabajo de un trabajadro, horas extras y su total

#Recibe horas normales y pago por hora y regresa pago normal
def calcularPagoNormal(horasN, pagoH):
    pagoN= horasN * pagoH
    return pagoN


#Recibe horas extra y pago por hora y regresa pago extra
def calcularPagoExtra(horasE, pagoH):
    pagoExtra= horasE * (pagoH * 1.85)
    return pagoExtra


#Recibe horas normales,  pago por hora, horas extra, pago normal, pago extra y los imprime
def imprimir(pagoNormal, pagoExtra):
    print("Pago Normal= %.2f $" % (pagoNormal))
    print("Pago Extra= %.2f $" % (pagoExtra))
    print("--------------------------------------")
    print("Pago Total= %.2f $"% (pagoExtra + pagoNormal))

#Principal, resuelve el problema
def main():
    horasN= int(input("Teclea las horas normales trabajadas :"))
    horasE= int(input("Teclea las horas Extras trabajadas :"))
    pagoH= int(input("Teclea el pago por hora :"))
    pagoNormal= calcularPagoNormal(horasN, pagoH)
    pagoExtra = calcularPagoExtra(horasE, pagoH)
    imprimir(pagoNormal,pagoExtra)

#Llama a la función main
main()

