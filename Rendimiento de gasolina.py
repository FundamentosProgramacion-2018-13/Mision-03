# Autor: Zabdiel Valentin Garduño Vivanco, A01377950
# Descripcion: sacar el rendimiento de un auto en kilimetros y millas.


def rendimiento (distancia, litros):#kilometros entre litro
    rendimiento= distancia/litros
    return rendimiento



def rendimiento2(distancia, galones):#millas entre galones
    distancia=distancia/1.6093       #conversion de kilometros a millas
    volumen=galones*0.264            #conversion de litros a galones
    rendimiento2=distancia/volumen
    return rendimiento2


def main():
    distancia=int(input("Teclea el numero de km recorridos: "))
    volumen=int(input("Teclea el numero de litros de gasolina usados: "))

    primerDato=rendimiento(distancia, volumen)
    segundoDato=rendimiento2(distancia, volumen)

    print("si recorres", distancia,"kms con", volumen,"""litros de gasolina el rendimiento es:
    %.2f"""% (primerDato),"km/l" """
    %.2f"""%(segundoDato),"mi/gal")

    tercerDato=int(input("¿Cuántos kilómetros vas a recorrer? "))

    gasolina= tercerDato/primerDato

    print("Para recorrer",tercerDato,"Km. Necesitas %.2f"%(gasolina),"litros de gasolina")#se imprime la gasolina que se necesitara.

main()





