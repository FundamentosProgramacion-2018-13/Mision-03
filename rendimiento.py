# Autor:Jesús Emmanuel Alcalá Nava
# Descripción: calcula la eficiencia de la gasolina segun los km viajados
def calcularKml(kilometros, litros):     #Kilometros sobre litros
    eficienciaKml = kilometros / litros
    return eficienciaKml
def calcularMg(kilometros, litros):       #Millas/galón
    eficienciaMg = kilometros/1.6093 / litros/.264
    return eficienciaMg
def calcularLitros(kilometros, litros, kilometrosViajados):
    eficiencia = kilometros / litros
    litrosNecesarios = kilometrosViajados / eficiencia
    return litrosNecesarios
def main():
    kilometros = int(input("Km viajados: "))
    litros = int(input("Litros de gasolina: "))
    eficienciaKml = calcularKml(kilometros, litros)
    eficienciaMg = calcularMg(kilometros, litros)
    print('''Si viajas %d kms con %d litros de gasolina, el rendimiento es: %.2f km/l %.2f mi/gal ''' % (kilometros, litros, eficienciaKml, eficienciaMg))
    kilometrosViajados = int(input("Cuántos kilómetros vas a viajar? "))
    litrosNecesarios = calcularLitros(kilometros, litros, kilometrosViajados)
    print('''Para viajar %d km. necesitas %.2f litros de gasolina''' % (kilometrosViajados, litrosNecesarios)) #imprimir resultados
main()