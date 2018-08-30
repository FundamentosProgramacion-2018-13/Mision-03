# Emiliano Heredia Garcia A01377072
# Calcula rendimiento en base de km y litros usados. Despues puede calcular litros requeridos para un recorrdio
# especifico.

def calcularRendimiento(km, litros):
    # Calcula el rendimiento con unidades Km/litros
    return km/litros

def calcularRendimientoMG(rendimiento):
    # Calcula el rendimiento con unidades millas/galones
    return rendimiento*(1/(1.6093*0.264))

def calcularLitrosNec(rendimiento, km):
    # Calcula los litros necesarios dado el rendimiento en km/litros y los km a recorrer.
    return km/rendimiento

def main():

    km = int(input("Teclea el número de km recorridos: "))
    litros = int(input("Teclea el número de litros de gasolina usados: "))

    rendimiento = calcularRendimiento(km, litros)
    rendimientoMG = calcularRendimientoMG(rendimiento)

    print("\nSi recorres %d kms con %d litros de gasolina, el rendimiento es:  " % (km, litros))
    print("%.2f km/l" % rendimiento)
    print("%.2f mi/gal" % rendimientoMG)

    kmR = int(input("¿Cuántos kilómetros vas a recorrer? "))

    ltrsN = calcularLitrosNec(rendimiento, kmR)

    print("Para recorrer %d km. necesitas %.2f litros de gasolina " % (kmR, ltrsN))



main()
