#Nombre: Saúl Figueroa Conde.
#Matrícula: A01747306.
#Programa: Este programa calcula el pago semanal de un trabajador, mostrando el pago normal, pago extra
#y pago total dependiendo de la cantidad de horas que haya trabajado.


#Se define la función que va a calcular el pago correspondiente a las horas normales (pagoNormal). Recibe como parámetros
#la cantidad de horas normales y el valor del pago por hora. Por último, la función regresa el valor de las horas normales.
def calcularNormal(n, p):
    normal = n * p
    return normal


#Se define la función que va a calcular el pago correspondiente a las horas extras (pagoExtra). Recibe como parámetros
#la cantidad de horas extras y el valor del pago por hora. Por último, la función regresa el valor de las horas extras.
def calcularExtra(e, p):
    extra = e * (p * 1.85) #Se multiplica el valor p * 1.85 ya que las horas extras vale 0.85% más que las normales.
    return extra

#Aquí se define la función main. El usuario indica la cantidad de horas normales trabajadas, las horas extras
#y el pago por hora. Los valores especificados se envían a las funciones de pagoNormal y pagoExtra para que regresen
#los valores del pago normal y el pago extra. Al final, imprime un espacio en blanco, para separar los datos de entrada
#de los de salida, imprime el valor del pago normal, el pago extra, una línea para separar el resultado final de los
#demás, y el valor del pago total. Cada valor con 2 decimales de precisión.
def main():
    horasNormales = float(input("Teclea las horas normales trabajadas: "))
    horasExtras = float(input("Teclea las horas extras trabajadas: "))
    pagoXHora = float(input("Teclea el pago por hora: "))

    normal = calcularNormal(horasNormales, pagoXHora)
    extra = calcularExtra(horasExtras, pagoXHora)

    print("")
    print("Pago normal: $%.2f" %(normal))
    print("Pago extra: $%.2f" % (extra))
    print("-----------------------")
    print("Pago total: $%.2f" %(normal + extra))

#El programa llama aquí a la función main para resolver el problema en cuestión, calculando el pago normal, el pago
#extra y el pago total dependiendo de la cantidad de horas trabajadas.
main()