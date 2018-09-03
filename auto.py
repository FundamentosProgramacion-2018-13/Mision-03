#encoding: UTF-8
#Autor: Alek Howland, A01747765
#Descripcion: Programa que calcula el rendimiento de combustible de un automovil

def calcularKmLitro(kmrec, gasut): #Calucla el redimiento en km/lt
    KmLitro = kmrec / gasut
    return KmLitro


def calcularMilGal(kmrec, gasut):   #Calcula el redimiento en mi/gal
    milGal = calcularKmLitro(kmrec, gasut)/ 1.6093/0.264
    return milGal


def imprimir1(kmrec, gasut, KmLitro, milGal):   #Imprime los resultados
    print("")
    print ("Si recorres %d kms con %d litros de gasolina, el rendimiento es: " % (kmrec, gasut))
    print ("%.2f km/l" % (KmLitro))
    print ("%.2f mi/gal" % (milGal) + "\n")




def calcularRendimientoUsuario(pregunta, Kmlitro):  #Calcula gasolina necesaria por km dados
    rendimiento = pregunta / Kmlitro
    return rendimiento


def imprimir2(pregunta, rendimiento):   #Imprime resultados

    print ("")
    print ("Para recorrer %d km. necesitas %.2f litros de gasolina" % (pregunta, rendimiento))


def main(): #Función principal
    kmrec = float(input("Teclea el número de km recorridos: "))
    gasut = float(input("Teclea el número de litros de gasolina usados: "))
    calcularKmLitro(kmrec, gasut)
    calcularMilGal(kmrec, gasut)
    imprimir1(kmrec, gasut, calcularKmLitro(kmrec, gasut), calcularMilGal(kmrec, gasut))
    pregunta = float(input("¿Cuántos kilómetros vas a recorrer? "))
    calcularRendimientoUsuario(calcularKmLitro(kmrec, gasut), pregunta)
    imprimir2(pregunta, calcularRendimientoUsuario(pregunta, calcularKmLitro(kmrec, gasut)))

main()  #Se llama a la función principal

