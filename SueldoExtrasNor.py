#Luisa Fernanda Arellano Alvarado

def calcularHorasNor(HorasN, sueldo):
    pagoN = HorasN*sueldo
    return pagoN



def calcularHorasExt(HorasE,sueldo):
    pagoE = sueldo*0.85*HorasE
    return pagoE

def main():
    
   ExtrasHrs = int(input("teclea horas extras trabajada:"))
   NormalesHrs = int(input("teclea horas normales trabajada:"))
   TotalHorasExtras = calcularHorasNor(ExtrasHrs,sueldoHora)
   TotalHorasNormales = calcularHorasNor(NormalesHrs,sueldoHora)
   total = TotalHorasExtras + TotalHorasNormales

   print("Pago hora normal:%.2f"% (TotalHorasNormales))
   print("Pago hora extra:%.2f"% (TotalHorasExtras))
   print("Pago Total:%.2f"% (total))

   

main()
