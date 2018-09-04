#Autor: Juan Sebastián Lozano Derbez
#Se calcula el cosato total de la compra de unos asientos

def calcboletosa(cantidada, cantidadb, cantidadc):          #Se calcula el total de todos los asientos
    total = 925*(cantidada) + 775*(cantidadb) + 360*(cantidadc)
    return total


#Se reciben las entradas y se imprime el resultado
def main():
    cantidada = int(input("Cuántos boletos A?: "))
    cantidadb = int(input("Cuántos boletos B?: "))
    cantidadc = int(input("Cuántos boletos C?: "))

    total = calcboletosa(cantidada, cantidadb, cantidadc)
    print("Total: ", total)
main()