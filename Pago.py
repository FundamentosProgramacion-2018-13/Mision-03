# Autor: Francisco Ariel Arenas Enciso
# Actividad : Cálculo del pago de un trabajador


'''
Esta función es la responsable de recibir los datos de entrada (horas normales y la cantidad que se paga por hora), de
la función main, los almacena en una variable y los usa para hacer las operaciones aritmeticas necesarias para devolver
el pago por las horas laborales rutinarias.
'''

def calcularHoras_normales(horas_normales, pago):
    horas_trabajadas = horas_normales * pago
    return horas_trabajadas


'''
Esta función es la responsable de recibir los datos de entrada (horas extra y la cantidad que se paga por hora), de 
la función main, los almacena en una variable y los usa para hacer las operaciones aritmeticas necesarias para devolver 
el pago por las horas laborales extra. 
'''

def calcularHoras_extra(horas_extra, pago):
    horasTrabajoExtra = (horas_extra*pago) * 1.85
    return horasTrabajoExtra


'''
Esta función es la responsable de recibir los datos de entrada (horas normales, horas extra y la cantidad que se paga 
por hora), de la función main, los almacena en una variables y los usa para hacer las operaciones aritmeticas necesarias
para devolver el pago total de un trabajador. 
'''

def calcularTotal_pago(horas_normales, horas_extra, pago):
    pago_total = calcularHoras_normales(horas_normales, pago) + calcularHoras_extra(horas_extra, pago)
    return pago_total


'''
Función main (Es la responsable del funcionamiento de todo el programa).
Primero le pide al usuario las horas trabajadas, las horas extra y cuanto paga por hora. Estos datos son enviados
a las funciones de calcular 'calcularHoras_normales', 'calcularHoras_extra' y 'calcularTotal_pago respectivamente para 
que éstas puedan hacer su labor. 
Finalmente imprime el pago normal, el pago extra y el pago total
'''

def main():
    horas_normales = int(input("Ingrese las horas normales trabajadas: "))
    horas_extra = int(input("Ingrese las horas extras trabajadas: "))
    pago = int(input("¿Cuánto es el pago por hora? "))
    pago_normal = calcularHoras_normales(horas_normales, pago)
    pago_extra = calcularHoras_extra(horas_extra, pago)
    pago_total= calcularTotal_pago(horas_normales, horas_extra, pago)
    print('Pago normal: $ %5.2f' % (pago_normal))
    print('Pago extra: $ %5.2f' % (pago_extra))
    print("---------------------------------")
    print('Pago total: $ %5.2f' % (pago_total))


main()

