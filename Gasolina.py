# Alex Fernando Leyva Martinez / A01747078
# Calcular el rendimiento en km/l y mi/gal de los autos

#Permite calcular el rendimiento en kilometros por litro
def rendimientolkm(kilometros, litros):
    lkm = (kilometros / litros)
    return lkm

#Permite calcular el rendimiento en millas por galón
def rendimientogalmi(kilometros, litros):
    galmi = (kilometros / (litros * 1.6093 * 0.264))
    return galmi

#Pregunta los datos y llama a las funciones anteriores
def main():
    kilometros = int(input("Teclea el número de km recorridos: "))
    litros = int(input("Teclea el número de litros de gasolina usados: "))
    lkm = rendimientolkm(kilometros,litros)
    galmi = rendimientogalmi(kilometros, litros)
    print("   ")
    print("Si recorres", kilometros, "kms con", litros, "de gasolina, el rendimiento es: ")
    print("%.2f km/l" % lkm)
    print("%.2f mi/gal" % galmi)
    print("   ")
    kmrecorrer = (int(input("¿Cuántos kilómetros vas a recorrer? ")))
    print("   ")
    ren = kmrecorrer / lkm
    print("Para recorrer", kmrecorrer, "km. necesitas %.2f" % ren, "litros de gasolina")

main()