# Autor: Francisco Ariel Arenas Enciso
# Actividad : Cálculo del total a pagar de boletos dependiendo de su clase

'''
Función que recibe los datos de entrada de la función main (número de boletos) como parametros, los alamcena en
variables y realiza las operaciones artimeticas necesarias para devolver datos de salida (total a pagar).
'''

def calcularPago (asientoA, asientoB, asientoC):
    pago_asientoA = asientoA * 925
    pago_asientoB = asientoB * 775
    pago_asientoC = asientoC * 360
    total_pago = pago_asientoA + pago_asientoB + pago_asientoC
    return total_pago


'''
Función main (Es la responsable del funcionamiento de todo el programa).
Primero le pide al usuario el número de boletos de cada clase de boletos. Posteriormente envía esos datos a la 
función defcalcularPago.

Finalmente imprime la cantidad de boletos de cada clase y el total a pagar.  
'''

def main():
    numero_boletosA = int(input('¿Cuántos boletos del tipo A se compraron? '))
    numero_boletosB = int(input('¿Cuántos boletos del tipo B se compraron? '))
    numero_boletosC = int(input('¿Cuántos boletos del tipo C se compraron? '))
    total_aPagar= calcularPago(numero_boletosA, numero_boletosB, numero_boletosC)
    print ("Número de boletos de clase A: ", str(numero_boletosA))
    print ("Número de boletos de clase B: ", str(numero_boletosB))
    print ("Número de boletos de clase C: ", str(numero_boletosC))
    print ("El costo total es: $ %5.2f" % (total_aPagar))


main()
