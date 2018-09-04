#Autor: Luis Mario Cervantes Ortiz
#Descripción: Calcular el pago semanal de un trabajador mas cuanto gana trabajando extra

def PagoNormal (horasN,horasP):#Calcular el pago normal
    PagoNormal=horasN*horasP
    return PagoNormal
def PagoExtra (horasE,horasP): #Calcular el pago extra
    PagoExtra=(horasE*horasP)*1.85
    return PagoExtra

def main(): #Preguntar datos
    horasN=int(input("Teclee las horas normales trabajadas: "))
    horasE=int(input("Teclee las horas extras trabajadas: "))
    horasP=int(input("Teclee el pago por hora: "))
#Summonear las funciones
    PagoTotalN=PagoNormal(horasN,horasP)
    PagoTotalE=PagoExtra(horasE,horasP)
#Calcular pago total
    PagoTotalT=PagoTotalN+PagoTotalE
    print("Pago normal: $ %.2f"%(PagoTotalN))
    print("Pago extra: $ %.2f"%(PagoTotalE))
    print("Pago total: $ %.2f"%(PagoTotalT))

main()