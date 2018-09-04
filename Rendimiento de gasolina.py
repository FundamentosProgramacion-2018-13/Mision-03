#Autor: Patricio Mondrgón
#Este programa calcula el rendimiento de gasolina de un auto.

# la siguiente funcion calcula el rendimiento en sistema internacional
def calcularelrendimientoensistemainternacional(numerodekm,numerodel):
    rendimientoenl= numerodekm/numerodel
    return rendimientoenl

#la  siguiente funcion calcula el numero de millas
def calcularmillas(numerodekm):
    numerodem= numerodekm/1.609
    return numerodem

#la siguiente funcion calcula el numero de galones
def calcularnumerodegalones(numerodel):
    numerodegalones= numerodel/3.78
    return numerodegalones

#lasiguiente funcion calcula el rendiminento en sistema ingles
def calcularrendimientoensistemaingles(numerodem,numerodegalones):
    rendimientoeng= numerodem/numerodegalones
    return rendimientoeng


def main():
    numerodekm= int(input("Tecle el numeor de kilometros que usaste:"))
    numerodel= int(input("Teclea el numero de litros de gasolina usada:"))
    rendimientoenl= calcularelrendimientoensistemainternacional(numerodekm,numerodel)
    numerodem =calcularmillas(numerodekm)
    numerodegalones= calcularnumerodegalones(numerodel)
    rendimientoeng=calcularrendimientoensistemaingles(numerodem,numerodegalones)
    print("Si recorres%.2f"%(numerodekm),"km con",numerodel,"entonces tu rendimiento es:%.2f"%(rendimientoenl),"km/l")
    print("y %.2f"%(rendimientoeng),"m/gl")

main()
