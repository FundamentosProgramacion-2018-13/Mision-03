# Autor: Ithan Alexis Pérez Sánchez
# Saber el rendimiento de nuestro auto y determinar los Litros necesarios para cierta distancia


# La linea de codigo empieza después de esta linea




def Calcular_El_Rendimiento(Kilometros, Gasolina): # ----------------------
    KmxL = Kilometros / Gasolina
    return KmxL

def Conversiones(Kilometros, Gasolina):     # Estas funciones determinar el calculo de lo que se desea tener
    Mi = Kilometros / 1.6093
    Gal = Gasolina * 0.264
    MixGal = Mi / Gal
    return MixGal

def Calcular_Litros(Kilometros, Gasolina, Litros): # ---------------------------
    Litros_Necesarios = (Litros * Gasolina) / Kilometros
    return Litros_Necesarios


def Imprimir_Resultados(KmxL, MixGal, Litros_Necesarios): # Imprime los datos solicitados
    print("Tu primer rendimiento es de: %.2f Km/L" % (KmxL))
    print("Convertido en Mi/Gal es de: %.2f Mi/Gal" % (MixGal))
    print("Lo Litros que necesitas para esta distancia son: %.2f L" % (Litros_Necesarios))

def Imprimir(Kilometros, Gasolina, Litros):     # Utiliza los datos para poder mostrar que nuestras funciones son correctas
    KmxL = Calcular_El_Rendimiento(Kilometros, Gasolina)
    MixGal = Conversiones(Kilometros, Gasolina)
    Litros_Necesarios = Calcular_Litros(Kilometros, Gasolina, Litros)
    Imprimir_Resultados(KmxL, MixGal, Litros_Necesarios)

def main():                         # Para introducir nuestros datos e interactuar con dichos datos
    Kilometros = int(input("Los Km que recorriste: "))
    Gasolina = int(input("Los L de gasolina usados: "))
    Litros = int(input("Los Km que recorriste en una cierta distancia: "))
    Imprimir(Kilometros, Gasolina, Litros)

main()
