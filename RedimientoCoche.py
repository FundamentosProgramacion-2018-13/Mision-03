#Luis Jonathan Rosas Ramos
#A01377942
# Cuanta gasolina gasta el coche en funcion a la distancia que recorre

# para calcular km/l divides kilometros entre los litros usados
def calcularKm(km,gas):
    kilometroLitro = km/gas
    return kilometroLitro

# calcualr Millas/galon
def calcularMiGa(km, gas):
    # ya que una milla es igual a 1.6093 km hacemos una conversion
    millas = km/1.6093
    # como un galon es igual a 0.264 hacemos la conversion dividiendo los litros usados entre los galones necesarios
    galon = gas*0.264
    # hacemos la division entre las millas por galon
    millasGalon = millas/galon
    return millasGalon

    #calculamos los litros necesarios por galon tomamos el dato de km/litro
def calcularLitros(nv):
    # calcularmos que los litros necesarios seran los kilometros a recorrer entre los kilometros necesarios por litro
    gas = nv/27.94
    return gas

def main():
    # preguntar los kilometros y los litros gastados
    km = float(input("Cuantos kilometros recorriste: "))
    gas = float(input("Cuanta gasolina gastaste: "))
    # calcular kilometros por litro y por galon
    kilometroLitro = calcularKm(km, gas)
    millasGalon = calcularMiGa(km,gas)
    print("Si recorres", km, "con", gas, "litros de gasolina, el redimiento es: ")
    print("                       ")
    #imprimir Km/litro
    print("%.2f"%kilometroLitro,"Km/l ")
    #imprimir millas/galon
    print("%.dF"%millasGalon,"mi/gal")
    nv =(float(input("¿Cuantos kilometros vas a recorrer?: ")))
    # calcular los litros necesarios en nv kilometros recorridos
    gasfinal = calcularLitros(nv)
    print("Para recorrer ", km,"km.","Necesitas %.2f" %gasfinal,"litro de gasolina")

main()