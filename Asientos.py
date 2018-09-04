# Autor: Ithan Alexis Pérez Sánchez
# Consulta de cuantos boletos quiere comprar un cliente


# La linea de codigo empieza después de esta linea

def Calcular_PagoTotal(Asientos_A, Asientos_B, Asientos_C): # Sirve para hacer la cuenta de cuantos boletos compramos
    Total = Asientos_A + Asientos_B + Asientos_C
    return Total

def Calcular_PrecioA(Asientos_A):               # ------------
    Asiento_A = Asientos_A * 925
    return Asiento_A

def Calcular_PrecioB(Asientos_B):               # Las 3 Funciones sirven para calcular el precio de cada tipo de asiento
    Asiento_B = Asientos_B * 775
    return Asiento_B

def Calcular_PrecioC(Asientos_C):               # -------------
    Asiento_C = Asientos_C * 360
    return Asiento_C

def Imprimir_Resultados(Asiento_A, Asiento_B, Asiento_C, Total):    # Nos manda a imprimir el precio, cantidad de boletos, y el Total
    print("Precio por clase A = %.2f" % (Asiento_A))
    print("Precio por clase B = %.2f" % (Asiento_B))
    print("Precio por clase C = %.2f" % (Asiento_C))
    print("Asientos por comprar = %.2f" % (Total))
    print("Pago Total es = %2.f" % (Asiento_A + Asiento_B + Asiento_C))

def Imprimir(Asientos_A, Asientos_B, Asientos_C, Calcular_PagoTotal):       # Mandamos a sacar los datos que queremos
    Precio_1 = Calcular_PrecioA(Asientos_A)
    Precio_2 = Calcular_PrecioB(Asientos_B)
    Precio_3 = Calcular_PrecioC(Asientos_C)
    Total = Calcular_PagoTotal
    Imprimir_Resultados(Precio_1, Precio_2, Precio_3, Total)

def main():                 # Ponemos variables para determinar nuestra función, ingresamos datos y esperamos el calculo
    Asientos_A = int(input("Cantidad de boletos de asientos para la clase A: "))
    Asientos_B = int(input("Cantidad de boletos de asientos para la clase B: "))
    Asientos_C = int(input("Cantidad de boletos de asientos para la clase C: "))
    Calcular_PagoTotal = Asientos_A + Asientos_B + Asientos_C
    Imprimir (Asientos_A, Asientos_B, Asientos_C, Calcular_PagoTotal)


main()