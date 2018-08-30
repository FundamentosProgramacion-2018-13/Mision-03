#Autor: Arturo Márquez Olivar. A01376086
#Calcula el pago de un trabajador.

#Calcula el pago por las horas normales trabajadas.
def calcularPagoNormal(horasNormales, pagoPorHora):
    pagoNormal= horasNormales * pagoPorHora
    return pagoNormal
    
#Calcula el pago por las horas extra trabajadas.
def calcularPagoExtra(horasExtra, pagoPorHora):
    valorHoraExtra= pagoPorHora * .85
    valorHoraExtra= valorHoraExtra + pagoPorHora 
    
    pagoExtra= horasExtra * valorHoraExtra
    return pagoExtra
    
#Es la función principal, se encarga de leer y de imprimir los datos.
def main():
    horasNormales= int(input("¿Cuántas horas normales fueron trabajadas?"))
    horasExtra= int(input("¿Cuántas horas extra fueron trabajadas?"))
    pagoPorHora= int(input("¿Cuál es el pago por hora?"))
    
    pagoNormal= calcularPagoNormal(horasNormales, pagoPorHora)
    pagoExtra= calcularPagoExtra(horasExtra, pagoPorHora)
    pagoTotal= pagoNormal + pagoExtra
    
    print("El pago de las horas normales es de: %.2f pesos." % (pagoNormal))
    print("El pago de las horas extra es de: %.2f pesos." % (pagoExtra))
    print("El pago total es de: %.2f pesos." % (pagoTotal))
    
#Llamada a la función principal.    
main()
    
    
