#Autor: Alberto Contreras Torres
#Calcula el monto total a pagar por el usuario por cada tipo de asiento


#Recibe los asientos solicitados y regresa el pagot total
def calcularPago(asientoA, asientoB, asientoC):
    calcularA = asientoA*925
    calcularB = asientoB*775
    calcularC = asientoC*360
    pagoTotal = calcularA + calcularB + calcularC
    return pagoTotal

#Recibe los asientos y el pago total y lo imprime
def imprimir(pagoTotal):
    print("El costo total es: %.2f $"% (pagoTotal))



#Principal, resuleve el problema
def main():
    asientoA= int(input("Teclea no. de asientos A :"))
    asientoB= int(input("Teclea no. de asientos B :"))
    asientoC= int(input("Teclea no. de asientos C :"))
    pagoTotal= calcularPago(asientoA, asientoB, asientoC)
    imprimir (pagoTotal)

#Llama a la función main
main()