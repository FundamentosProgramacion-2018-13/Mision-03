#Autor: Alberto Contreras Torres
#Calcula la cantidad de litros de gasolina usados en base a los kilometros recorridos

#Recibe kilometros y litros de gasolina utilizados y regresa rendimiento en kilometros/litro
def calcularRendimientoAutoKm(km, lG):
    rendimientoKm= km / lG
    return rendimientoKm

#Recibe kilometros y litros de gasolina utilizados y regresa rendimiento de auto en millas/galón
def calcularRendimientoAutoMi(km, lG):
    milla= (km*1)/1.6093
    galon= (lG*.264)/1
    rendimientoMi= milla/galon
    return rendimientoMi

#Recibe kilometros, litros de gasolina utilizada y kilometros a recorrer y regresa litros necesarios
def calcularKmViaje (km, lG, kmR):
    rendimientoKm= calcularRendimientoAutoKm(km, lG)
    litrosN= kmR/rendimientoKm
    return litrosN

#Recibe kilometros, litros de gasolina utilizados, rendimiento de auto en millas/gaón, rendimeinto de auto en kilometro/litro y los imprime
def imprimir(km,lG,rendimientoKm,rendimientoMi):
    print("Si recorres", km,"kms con", lG,"litros de gasolina, el rendimiento es:")
    print("%.2f"%(rendimientoKm), "km/l")
    print("%.2f"% (rendimientoMi), "mi/gal")

#Recibe kmR, litrosN y los imprime
def imprimir2(kmR,litrosN):
    print("Para recorrer", kmR, "km. necesitas","%.2f"% (litrosN), "litros de gasolina")


#Principal, resuelve el problema
def main():
    km= int(input("Teclea no. de km recorridos :"))
    lG= int(input("Teclea no. de litros de gasolina utilizada :"))
    rendimientoKm= calcularRendimientoAutoKm(km, lG)
    rendimientoMi = calcularRendimientoAutoMi(km, lG)
    imprimir (km,lG,rendimientoKm,rendimientoMi)
    kmR= int(input("¿Cuántos km vas a recorrer? :"))
    litrosN = calcularKmViaje(km, lG, kmR)
    imprimir2 (kmR, litrosN)

#Llamar a la función main
main()

