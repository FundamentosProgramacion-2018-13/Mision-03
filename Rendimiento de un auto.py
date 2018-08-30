#Nombre: Saúl Figueroa Conde.
#Matrícula: A01747306.
#Programa: Este programa calcula el rendimiento de un auto con base en la cantidad de km. que recorre y la
#cantidad de gasolina utilizada (valores que son indicados por el usuario). Después el programa imprime la
#cantidad de litros necesarios para recorrer la cantidad de kilómetros que especifique el usuario.

#Se define la función que va a calcular el rendimiento del vehículo en km/l. Los parámetros que recibe la función son
#la cantidad de kilómetros recorridos y la cantidad de litros usados. Al final, la función regresa el valor del rendimiento
#en km/hr.
def calcularRendimientoA(k, l):
    km_l = k / l
    return km_l

#Se define la función que va a calcular el rendimiento del vehículo en mi/gal. Los parámetros que recibe la función son
#la cantidad de kilómetros recorridos y la cantidad de litros usados, al igual que la función anterior. Al final, la
# función regresa el valor del rendimiento en mi/gal.
def calcularRendimientoB(k, l):
    mi_gal = (k / l) * 2.3538 #Este es el factor de conversión (estadounidense) de km/l a mi/gal.
    return mi_gal

#Aquí se define la función que calcurará la cantidad de litros necesarios para realizar un viaje con base en el
#parámetro de kms indicado por el usuario. Al final, la función regresa el valor de los litros necesarios para tal viaje.
def calcularLitros(k, r):
    litrosNecesita = k / r
    return litrosNecesita

#Aquí se define la función main. Primero lee los valores para kms y litros que indica el usuario. Posteriormente, envía
#estos valores a las funciones calcularRendimientoA y calcularRendimientoB. Después imprime el valor correspondiente
#al rendimiento del vehículo con una precisión de 2 decimales. También se incluyen espacios en blanco para hacer
#separar la información y que sea más fácil su lectura. Después de lo anterior, la función pregunta al usuario
#la cantidad de kms que va a viajar el usuario. Este valor se envía a la función calcularLitros y por útlimo se
#imprime en pantalla.
def main():
    km = int(input("Teclea el número de km recorridos: "))
    litros = int(input("Teclea el número de litros de gasolina usados: "))
    km_l = calcularRendimientoA(km, litros)
    mi_gal = calcularRendimientoB(km, litros)

    print("")
    print("Si recorres {} kms con {} litros de gasolina, el rendimiento es: ".format(km, litros))
    print("{:0.2f} km/l".format(km_l))
    print("{:0.2f} mi/gal".format(mi_gal))
    print("")

    recorrer = int(input("¿Cuántos kilómetros vas a recorrer? "))
    litrosNecesita= calcularLitros(recorrer, km_l)
    print("")
    print("Para recorrer {} km. necesitas {:0.2f} litros de gasolina".format(recorrer, litrosNecesita))

#Se llama a la función main para resolver el problema en cuestión por medio de los comandos previamente
#especificados en las funciones anteriores.
main()