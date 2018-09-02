# Mariana Caballero Cabrera A01376544

# A continuación voy a escribir un programa que calcule el pago a un trabajador dependiendo de las horas de trabajo




# esta función calcula el pago normal por hora

def pagoNormal (horas, pagoHora):
    pagoN = horas*pagoHora
    return pagoN



#esta función calcula el pago por horas extras trabajadas

def pagoExtra(horasExtras, pagoHora):
    pagoE = (pagoHora*.85 + pagoHora)*horasExtras
    return pagoE


#esta función calcula el total para pagar por las horas que trabajó

def pagoTotal( pagoN, pagoE):
    pagoT = pagoN + pagoE
    return pagoT



#esta función imprime los resultados

def imprimir(pagoN, pagoE, pagoT):

    print ("Pago normal:  $%5.2f" % (pagoN))
    print("Pago Extra:  $%5.2f" % (pagoE))
    print ("------------------------------")
    print("Pago Total:  $%5.2f" % (pagoT))


# función principal

def main():

    horas = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))

    pagoN = pagoNormal (horas, pagoHora)
    pagoE = pagoExtra(horasExtras, pagoHora)
    pagoT =  pagoTotal( pagoN, pagoE)

    imprimir (pagoN, pagoE, pagoT)



# llamamos a la función

main()
