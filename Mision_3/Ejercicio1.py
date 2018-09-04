# Autor: Roberto Emmanuel González Muñoz
# Hay 3 clases de asientos en un estadio de fútbol. La clase A cuesta $925, la clase B cuesta $775 y la clase C
# cuesta $360. Escribe un programa que pregunte al usuario cuántos boletos quiere comprar para cada tipo de
#  asiento y que imprima el total a pagar.

def calcularpago(asientosA, asientosB, asientosC):
    costo_asientos_a = 925 * asientosA
    costo_asientos_b = 775 * asientosB
    costo_asientos_c = 360 * asientosC
    total_pago = costo_asientos_a + costo_asientos_b + costo_asientos_c
    return total_pago


def main():
    numero_boletos_a = input(int("Cuántos boletos clase A necesita? "))
    numero_boletos_b = input(int("Cuántos boletos clase B necesita? "))
    numero_boletos_c = input(int("Cuántos boletos clase C necesita? "))
    resultado = calcularpago(numero_boletos_a, numero_boletos_b, numero_boletos_c)
    print("Número de boletos clase A: #d" % numero_boletos_a)
    print("Número de boletos clase B: #d" % numero_boletos_b)
    print("Número de boletos clase C: #d" % numero_boletos_c)
    print("El costo total de sus boletos es: %d" % resultado)


main()
