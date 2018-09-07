#Luisa Fernanda Arellano Alvarado A01377974

def calcularArea(altura,baseM,basem):
    AreaTrapecio = (baseM + basem)/2*altura
    return AreaTrapecio





def calculaPerimetro(altura,baseM,basem):
    LadosT = (((baseM - basem)/2)**2 + altura**2)** 1/2*2
    PerimetroTrapecio = baseM + basem + LadosT
    return PerimetroTrapecio


def main ():
    baseMayor = int(input("teclea la longitud de la base mayor:"))
    baseMenor = int(input("teclea la longitud de la base menor:"))
    altura = float(input("teclea la altura:"))
    area = calcularArea(altura,baseMayor,baseMenor)
    perimetro = calculaPerimetro(altura,baseMayor,baseMenor)
    print ("Area:%.2f"%(area))
    print ("Perimetro:%.2f"%(perimetro))
           
#Llamamos a la función main
main()

           
