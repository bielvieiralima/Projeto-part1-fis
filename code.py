from math import *

c = 3*(10**8)
pi = 3.1415

def Freq():
    f = float(input("Digite a frequência da onda: "))
    λ = c/f
    w = 2*pi*f
    k = w/c

    print("\nO comprimento de onda é %.3f m" %λ)
    print("O tipo de onda é: ", end='')

    if f >= (10**20):
        print("Raios Gama")
    elif f >= (10**18):
        print("Raios-X")
    elif f >= (10**16):
        print("Luz Ultravioleta")
    elif f >= (10**12):
        print("Luz Infravermelho")
    elif f >= (10**10):
        print("Microondas")
    else:
        print("Rádio")

    print("O valor de w é de %.3f rad/s" %w)
    print("O número da onda (k) é %.9f" %k)

def comprimento_de_onda():
    comprimento = float(input("Digite o comprimento de onda: "))
    print()
    print("Escolha a unidade de medida :")
    print("1 - [nm]")
    print("2 - [µm]")
    print("3 - [mm]")
    print("4 - [m]")
    print("5 - [km]")
    opcao = int(input())
    if opcao == 1:
        comprimento = comprimento *(10**-9)
        print(comprimento)
    elif opcao == 2:
        comprimento = comprimento *(10**-6)
        print(comprimento)
    elif opcao == 3:
        comprimento = comprimento *(10**-3)
        print(comprimento)
    elif opcao == 4:
        print(comprimento)
    elif opcao == 5:
        comprimento = comprimento *(10**3)
        print(comprimento)
    
    frequencia = comprimento / c
    k = (2*pi) / comprimento
    w = (2*pi) * c

    print("A frequência é igual a: %.3f\n" % frequencia)
    print("O número de ondas é igual a: %.3f\n" % k)
    print("A frequência angular é igual a: %.3f\n" % w)

def main():
    while True:
        print("1 - Usar o comprimento de onda")
        print("2 - Usar a frequência")
        print("0 - Encerrar o programa")

        x = int(input())

        if x == 1:
            comprimento_de_onda()

        if x == 2:
            funcao2()

        if x == 0:
            break

main()
