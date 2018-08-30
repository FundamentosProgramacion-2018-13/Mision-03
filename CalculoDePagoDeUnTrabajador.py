#Jesús Roberto Herrera Vieyra // A01377230
#Programa para calcular pago

#calcular pago de horas normales
def calcularHorasNormales(horasN,pago):
    salario = horasN*pago
    return salario

#calcular pago de horas extra
def calcularHorasExtra (horasE,pago):
    salario = horasE*pago*1.85
    return salario

#función principal
def main():
    horasN = int(input("Teclea las horas normales trabajadas: "))
    horasE = int(input("Teclea las horas extra trabajadas: "))
    pago = int(input("Teclea el pago: "))

    horasNormales = calcularHorasNormales(horasN,pago)
    horasExtra = calcularHorasExtra(horasE,pago)
    salario = horasNormales+horasExtra

    print("Pago normal: $""{0:.2f}".format(horasNormales))
    print("Pago extra: $""{0:.2f}".format(horasExtra))
    print("Pago total: $""{0:.2f}".format(salario))

main()