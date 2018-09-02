# Alex Fernando Leyva Martinez / A01747078
# Calcular el área y perimetro del trapecio

#Permite calcular el área de la figura
def area(baseMayor, baseMenor, altura):
    are = ((baseMayor + baseMenor)/2) * altura
    return are

#Permite calcular el perimetro de la figura
def perimetro(baseMayor, baseMenor, altura):
    a = ((baseMayor - baseMenor) / 2)
    lad = (a ** 2 + altura ** 2) ** 0.5
    per = baseMenor + baseMayor + 2*lad
    return per

#Pregunta los datos y llama a las funciones anteriores
def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    are = area(baseMayor, baseMenor, altura)
    per = perimetro(baseMenor, baseMayor, altura)
    print("Área: %.2f" % are)
    print("Perímetro: %.2f" % per)

main()