#Autor: Marco González Elizalde
'''Proposito: Calcula el pago de un trabajador basado en las horas
normales y extras trabajadas, considerando la cantidad que se le paga por hora'''

#Calcula el pago de las horas normales trabajadas
def pagoNormal(horasNormales, pagoXHora):
    pagoNormal = horasNormales * pagoXHora
    return pagoNormal

#Calcula el pago de las horas extras trabajadas, 1 hora extra = 1.85 hora normal
def pagoExtra(horasExtra, pagoXHora):
    pagoExtra = horasExtra * pagoXHora * 1.85
    return pagoExtra

'''Pregunta por el pago por hora, horas normales y extra trabajadas
e imprime el pago normal extra y total'''
def main():
    horasNormales = float(input("Teclea las horas normales trabajadas: "))
    horasExtra = float(input("Teclea las horas extras trabajadas: "))
    pagoXHora = float(input("Teclea el pago por hora: "))
    print("")

    pago_normal = pagoNormal(horasNormales, pagoXHora)
    pago_extra = pagoExtra(horasExtra, pagoXHora)
    pagoTotal = pago_normal + pago_extra

    print("""Pago normal: $%.02f
Pago extra: $%.02f
-----------------------
Pago total: $%.02f""" %(pago_normal,pago_extra,pagoTotal))

#Corre el programa
main()
