#Autor: Luis Mario Cervantes Ortiz
#Descripción: Preguntar sobre los kilometros y litros consumidos para mostrar rendimiento en km/l y mi/gal, además de mostrar los litros requeridos para recorrer cierto numero de km

def rendimientoKm(km,litros): #Kilometros/litros
    rendimientoKm=km/litros
    return rendimientoKm

def rendimientoMi(km,litros): #Mi/gal
    mi=km/1.6093
    gal=0.264*litros
    rendimientoMi=mi/gal
    return rendimientoMi
def main(): #Preguntar datos
    km= int(input("Teclea el numero de km recorridos: "))
    litros= int(input("Teclea el numero de litros de gasolina usados: "))
#Summonear las funciones
    totalkmRendi=rendimientoKm(km,litros)
    totalmiRendi=rendimientoMi(km,litros)

    print("Si recorres ",km, "kms con", litros,"""de gasolina, el rendimiento es:
    %.2f"""%(totalkmRendi),"km/l" """
    %.2f"""%(totalmiRendi),"mi/gal")
#Calcular la gasolina requerida
    Totalderecorrido=int(input("¿Cuántos kilómetros vas a recorrer?: "))
    totalgasolina=Totalderecorrido/totalkmRendi

    print("Para recorrer",Totalderecorrido,"necesitas %.2f"%(totalgasolina),"litros de gasolina")

main()