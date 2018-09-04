#Autor: Alan Diaz Carrera
#Descripcion: Calcular el pago de un trabajador

horasNor = int(input("Teclea las horas normales trabajadas:"))
horasEx = int(input("Teclea las horas extras trabajadas:"))
pagoHora = int(input("Teclea el pago por hora:"))

def main():
    pagoNor = int(horasNor*pagoHora)
    pagoEx=int(horasEx*(pagoHora*1.85))
    pagoTotal=pagoEx+pagoNor
    print("Pago normal: $%.2f"%(pagoNor))
    print("Pago extra: $%.2f"%(pagoEx))
    print("-----------------------")
    print("Pago total: $%.2f"%(pagoTotal))

mian()