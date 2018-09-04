# Autor: Ithan Alexis Pérez Sánchez
# Calcular el pago de un trabajador con horas extras incluidas


# La linea de codigo empieza después de esta linea

def Calcular_Pago_Normal(Horas_Normales, PagoxHora):    # --------------
    Pago = Horas_Normales * PagoxHora
    return Pago

def Calcular_Pago_Extras(Horas_Extras, PagoxHora):     # Las 3 funciones sirven para hacer el calculo de lo que queremos
    Pago_E = Horas_Extras * ((PagoxHora * 0.85) + PagoxHora)
    return Pago_E

def Total(Horas_Normales, Horas_Extras, PagoxHora):     # --------------
    Pago_Total = Calcular_Pago_Normal(Horas_Normales, PagoxHora) + Calcular_Pago_Extras(Horas_Extras, PagoxHora)
    return Pago_Total

def Imprimir_Resultado(Pago, Pago_E, Pago_Total):   # La impresión de nuestras incognitas para saber los datos correspondientes
    print("Pago Normal es = %.2f" % (Pago))
    print("Pago Extra es = %.2f" % (Pago_E))
    print("Pago Total es = %.2f" % (Pago_Total))

def Imprimir(Horas_Normales, Horas_Extras, PagoxHora):  # Lo que queremos que imprima una vez teniendo el calculo de los datos
    Pago = Calcular_Pago_Normal(Horas_Normales, PagoxHora)
    Pago_E = Calcular_Pago_Extras(Horas_Extras, PagoxHora)
    Pago_Total = Total(Horas_Normales, Horas_Extras, PagoxHora)
    Imprimir_Resultado(Pago, Pago_E, Pago_Total)

def main():                                # Nuestra principal función para ingresar datos y determinar el calculo
   Horas_Normales = int(input("Horas de jornada laboral trabajadas: "))
   Horas_Extras = int(input("Horas de jornada laboral trabajadas: "))
   PagoxHora = int(input("Horas de jornada laboral trabajadas: "))
   Imprimir(Horas_Normales, Horas_Extras, PagoxHora)

main()