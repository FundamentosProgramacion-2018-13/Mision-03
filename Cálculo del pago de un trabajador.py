#Rodolfo Anibal Altamirano Sánchez, A01377949
#Se busca saber cuanto gána un trabajador dandote las horas normales y horas extra que trabajo, así como el sueldo base.


#Calcula el pago que le corresponde a sus horas normales
def calcularPagoNormal(horasNormales, pagoPorHora):
    pagoNormal = horasNormales*pagoPorHora
    return pagoNormal

#Calcula el pago que le corresponde a sus horas extra
def calcularPagoExtra(horasExtra, pagoPorHora):
    pagoExtra = pagoPorHora*1.85*horasExtra
    return pagoExtra
#Calcula el pago ttal que le corresponde suando todo
def calcularPagoTotal(horasExtra,horasNormales,pagoPorHora):
    pagoExtra = calcularPagoExtra(horasExtra, pagoPorHora)
    pagoNormal = calcularPagoNormal(horasNormales, pagoPorHora)
    pagoTotal = pagoExtra+pagoNormal
    return pagoTotal

#Llama todas las funciones
def main():
    #Pide las variables de sueldo por hora, horas extra y horas normales trabajadas
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtra = int(input("Teclea las horas extra trabajadas: "))
    pagoPorHora = int(input("Teclea el pago por hora: "))

    pagoNormal = calcularPagoNormal(horasNormales, pagoPorHora)
    pagoExtra = calcularPagoExtra(horasExtra, pagoPorHora)
    pagoTotal = calcularPagoTotal(horasExtra,horasNormales,pagoPorHora)

    #Imprime todos los valores
    print("Pago normal: $%.2f"% pagoNormal)
    print("Pago eXtra: $%.2f"% pagoExtra)
    print("__________________________________________________________________")
    print("Pago total: $%.2f"% pagoTotal)




main()
