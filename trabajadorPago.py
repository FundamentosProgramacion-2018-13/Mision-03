# Luis Jonathan Rosas Ramos y Miguel Anguel Ramos Mendoza
# Calcular lo que se pagara a un trabajador, si este cumplio con horas extras o no

# funcion para calcular las horas normales
def pagarNormal(horasNormales,pagoHoras):
    # sera igual a las horas normales por el precio que le paguen
    HorasNormal = horasNormales*pagoHoras
    return HorasNormal

def pagarExtra(horasExtras,pagoHora):
    # debido a que las horas extras se pagan en %85 mas estas horas extras seran igual
    # a las mimsas horas mas el %85 por lo tanto se multiplica por 1.85
    horasExtras = horasExtras*(pagoHora*1.85)
    return horasExtras

def main():
    # preguntar las horas normales, extras y cuanto cobra por hora
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Pago por hora: "))
    HorasNormal = pagarNormal(horasNormales, pagoHora)
    HorasExtra = pagarExtra(horasExtras,pagoHora)
    total = HorasNormal+HorasExtra
    #imprimir los resultados
    print("Pago Normal: $ %.2f" %HorasNormal)
    print("Pago extra: $ %.2f" %(HorasExtra))
    print("-------------------------------")
    print("Pago total: $ %.2f"%total)

# llamar a la funcion main
main()