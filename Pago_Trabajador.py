#Autor: David rodriguez
#Calcula el salario semanal de un trabajador tomando en cuenta el pago de horas normales y horas extras

#Calcula el pago por las horas extras trabajadas
#Tomando en cuenta que se paga 85% más por hora
def CalcularPagoHorasExtras(pagoPorHora, horasExtras):
    extra = pagoPorHora*1.85
    pagoHorasExtras = horasExtras*extra
    return pagoHorasExtras

#Calcula el pago por las horas normales trabajadas
def CalcularPagoHorasNormales(pagoPorHora, horasNormales):
    pagoHorasNormales = pagoPorHora*horasNormales
    return pagoHorasNormales

#Imprime el pago normal, el pago extra y el pago total
def imprimir(pagoHorasNormales, pagoHorasExtras):
    print("Pago normal: $%.2f"%(pagoHorasNormales))
    print("Pago extra: $%.2f"%(pagoHorasExtras))
    print("-----------------------")
    print("Pago total: $%.2f"%(pagoHorasExtras+pagoHorasNormales))


def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoPorHora = int(input("Teclea el pago por hora: "))
    pagoHorasNormales = CalcularPagoHorasNormales(pagoPorHora,horasNormales)
    pagoHorasExtras = CalcularPagoHorasExtras(pagoPorHora, horasExtras)
    imprimir(pagoHorasNormales, pagoHorasExtras)

#Llama a la función principal
main()
