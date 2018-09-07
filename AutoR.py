#Autor: Luisa Fernanda Arellano Alvarado A01377974


def calcularRendimiento(km,l):
    Rendimiento = km/l
    return Rendimiento


def calcularRendimiento2(km,l):
    Rendimiento2 = (km/1.6093)/(l*0.264)
    return Rendimiento2

def calcularKilometros(km,l,distancia):
    litros = distancia*l/m
    return litros

def main():
   kilometros =float(input("Teclea el número de km recorridos: "))
    litros = float(input("Teclea el número de litros  usados: "))
    km= calcularRendimiento(kilometros,litros)
    l =calcularRendimientoConversion(kilometros,litros)
    print("kilometros recorridos son:%.2f"%(km))
    print("litros usados son: %.2f"%(l))
   

main()
