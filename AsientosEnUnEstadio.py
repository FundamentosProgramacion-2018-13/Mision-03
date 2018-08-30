#Jesús Roberto Herrera Vieyra // A01377230
#Calcular precio de asientos

#función para calcular el costo de los boletos
def CalcularPago(boletosA,boletosB,boletosC):
    Totalpago = boletosA*925+boletosB*775+boletosC*360
    return Totalpago


#funcion principal
def main():
    boletosA = int(input("Número de boletos de clase A: "))
    boletosB = int(input("Número de boletos de clase B: "))
    boletosC = int(input("Número de boletos de clase C: "))

    precioTotal = CalcularPago(boletosA,boletosB,boletosC)

    print("El costo total es: $""{0:.2f}".format(precioTotal))

main()