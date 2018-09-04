#Autor: Patricio Mondragón
# Este programa calcula el pago de un trabajador


def calcularelpagodehorasnormales(horastrabajadas,pagoporhora):
    pagonormal= pagoporhora*horastrabajadas
    return pagonormal


def calcularpagoextra(horastrabajadas ,pagoporhora):
    pagoporhoraextra= (pagoporhora)*5+(pagoporhora*.85)*5
    pagototalporhorasextra= horastrabajadas+pagoporhoraextra
    return pagototalporhorasextra




def main():
    horastrabajadas= int(input("Tecle el numero de horas trabajadas:"))
    horasextras= int(input("Teclea el numero de horas extra:"))
    pagoporhora= int(input("teclea el pago por hora:"))
    pagonormal= calcularelpagodehorasnormales(horastrabajadas,pagoporhora)
    pagototalporhorasextra= calcularpagoextra(horastrabajadas,pagoporhora)
    pagototal=pagonormal+pagototalporhorasextra
    print("El pagonormal es:",pagonormal)
    print("El pago extra es:",pagototalporhorasextra)
    print("El pago total es:",pagototal)

main()