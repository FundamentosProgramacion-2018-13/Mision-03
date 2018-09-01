# Autor: Francisco Ariel Arenas Enciso
# Actividad : Cálculo y demostración del rendimiento de un auto


'''
Esta función recibe los datos de entrada (km recorridos y litros usados) y estos son almacenados en una variable, la cual
calcula mediante operaciones aritmeticas el rendimiento del auto en km.
Éste último dato es regresado.
'''

def calcularRendimiento_km(km_recorridos, litros_usados):
    rendimiento = km_recorridos / litros_usados
    return rendimiento


'''
Esta función recibe los datos de entrada (km recorridos y litros usados)y son almacenados en una variable, la cual 
calcula mediante operaciones aritmeticas el rendimitno del auto en mi.
Éste último dato es regresado.
'''

def calcularRendimiento_mi(km_recorridos, litros_usados):
    rendimeinto_galones = km_recorridos / litros_usados
    conversion = (rendimeinto_galones / 1.6093) / 0.264
    return conversion


'''
Esta función recibe los datos de entrada originales (km recorridos y litros usados) así como el nuevo dato (km a recorrer)
y son almacenados en una variable, la cual calcula mediante operaciones aritmeticas la cantidad de litros necesarios.
Éste último dato es regresado.
'''

def calcularLitros_necesarios(num_km_a_recorrer, num_km_recorridos, num_litros_usados):
    litros_necesarios = num_km_a_recorrer / calcularRendimiento_km(num_km_recorridos, num_litros_usados)
    return litros_necesarios


'''
Función main (Es la responsable del funcionamiento de todo el programa).
Primero le pide al usuario la cantidad de km que ya recorrió, así como el número de litros usados(datos de entrada),
estos datos son enviados a las funciones 'calcularRendimiento_km', 'calcularRendimiento_mi' y 'calcularLitros_necesarios'
para que éstas puedan realizar sus respectivas tareas.
Posteriormente imprime el rendimiento del auto en dos unidades diferentes (km y mi)
Luego, vuelve a preguntarle al usuario por los km que desea recorrer, y éste dato es enviado a la función 
'calcularLitros_necesarios'.
Finlamente, imprime la cantidad de kilometros necesarios para poder recorrer los kilometros previamente dados.  
'''

def main():
    num_km_recorridos = int(input('Teclea el número de km recorridos: '))
    num_litros_usados = int(input('Teclea el número de litros usados: '))
    rendimiento_km = calcularRendimiento_km(num_km_recorridos, num_litros_usados)
    rendimiento_mi = calcularRendimiento_mi(num_km_recorridos, num_litros_usados)
    print('Si recorres %5.2f' % (num_km_recorridos),'km con %5.2f' % (num_litros_usados),'litros de gasolina, el rendimeinto será de: %5.2f' % (rendimiento_km), 'km/l, ó %5.2f' % (rendimiento_mi),'mi/gal')
    num_km_a_recorrer = int(input('Teclea cuántos kilometros va a recorrer: '))
    litros_necesarios = calcularLitros_necesarios(num_km_a_recorrer, num_km_recorridos, num_litros_usados)
    print('Para recorrer %5.2f' % (num_km_a_recorrer),'km, se van a necesitar %5.2f' % (litros_necesarios),'litros de gasolina')


main()

