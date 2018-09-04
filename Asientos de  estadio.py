# Autor: Patricio Mondragón
#El siguiente programa calcula el precio de distintos tipos de asientos y arroja el resultado.

def calcularprecioa(numerodeboletosA):
    precioboletosa= numerodeboletosA*925
    return precioboletosa


def calcularpreciob(numerodeboletosb):
    precioboletosb= numerodeboletosb*775
    return precioboletosb


def calcularprecioboletosc(numerodeboletosc):
    precioboletosc=numerodeboletosc*360
    return precioboletosc


def calcularcostototal(precioboletosa,precioboletosb,precioboletosc):
    costototal= precioboletosa+precioboletosb+precioboletosc
    return costototal


def main():
   numerodeboletosA =  float(input("¿Cuantos boletos de de tipo a va a querer?"))
   numerodeboletosb= int(input("Cuantos boletos tipo b va a querer?"))
   numerodeboletosc = int(input("Cuantos boletos tipo c va a querer?"))
   precioboletosa = calcularprecioa(numerodeboletosA)
   precioboletosb= calcularpreciob(numerodeboletosb)
   precioboletosc= calcularprecioboletosc(numerodeboletosc)
   costototal = calcularcostototal(precioboletosa,precioboletosb,precioboletosc )

   print( "El numero de boletos de clase A es:",numerodeboletosA)
   print ("El numeor de boletos clase B es:",numerodeboletosb)
   print("El numeor de boletos clase c es:", numerodeboletosc)
   print("El costo total es de:",costototal)


main()