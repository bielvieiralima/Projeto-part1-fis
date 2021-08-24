from math import *
from math import pi

c = 3*(10**8)


def Freq():
    f = float(input("Digite a frequência da onda: "))
    λ = c/f
    w = 2*pi*f
    k = w/c

    print("\nO comprimento de onda é m", format(λ, '.1E'))
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

    print("O valor de w é de ", format(w, '.1E'))
    print("O número da onda (k) é", format(k, '.1E'))

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
        comprimento = comprimento *(10**(-9))
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
    
    frequencia = c/comprimento
    k = (2*pi) / comprimento
    w = (2*pi) * frequencia

    print("A frequência é igual a:", format(frequencia, '.1E'))
    print("O número de ondas é igual a: %.3f\n" % k)
    print("A frequência angular é igual a: " , format(w, '.1E'))

def numero_onda():
    k = float(input("Digite o número de onda (K): "))

    λ = (2*pi)/k
    f = c/λ
    w = 2*pi*f

    if f >= (10**20):
        tipo = "Raios Gama"
    elif f >= (10**18):
        tipo = "Raios-X"
    elif f >= (10**16):
        tipo = "Luz Ultravioleta"
    elif f >= (10**12):
        tipo = "Luz Infravermelho"
    elif f >= (10**10):
        tipo = "Microondas"
    else:
        tipo = "Rádio"

    print("Valor da frequência = %.3f hz" %f)
    print("O comprimento de onda equivale a %.2f m" %λ)
    print("O tipo de onda é: %s" %tipo)
    print("A frequência angular da onda é: %.3fº" %w)

def freq_angular():
    w = float(input("Digite a frequência angular da onda (w): "))
    f = w/(2*pi)
    λ = c/f
    k = (2*pi)/λ

    if f >= (10**20):
        tipo = "Raios Gama"
    elif f >= (10**18):
        tipo = "Raios-X"
    elif f >= (10**16):
        tipo = "Luz Ultravioleta"
    elif f >= (10**12):
        tipo = "Luz Infravermelho"
    elif f >= (10**10):
        tipo = "Microondas"
    else:
        tipo = "Rádio"

    print("Valor da frequência = %.3f hz" %f)
    print("O comprimento de onda equivale a %.2f m" %λ)
    print("O tipo de onda é: %s" %tipo)
    print("o número de onda (K) é igual a %.3f" %k)


def campo_Bm():
    print('''Instruções:
    Caso deseje digitar o valor exponencial digite "e+" ou "e-" e então o expoente.
    Exemplo: 4.45 * 10⁵ deve ser digitado como 4.45e+5''')
    Em = float(input("Digite o valor do Campo Em: "))
    Bm = Em/c

    print("O valor do campo de Bm é igual a ", (format(Bm, '.1E'), 'T'))

def campo_Em():
    print('''Instruções:
    Caso deseje digitar o valor exponencial digite "e+" ou "e-" e então o expoente.
    Exemplo: 4.45 * 10⁵ deve ser digitado como 4.45e+5''')
    Bm = float(input("Digite o valor do Campo Bm: "))
    Em = Bm*c

    print("O valor do campo de Bm é igual a", (format(Em, '.1E'), "V/m\n"))

def main():
    while True:
        print("1 - Usar o comprimento de onda")
        print("2 - Usar a frequência")
        print("3 - Usar a número de onda (K)")
        print("4 - Cálculo do campo Bm (Entrada: Em)")
        print("5 - Cálculo do campo Em (Entrada: Bm)")
        print("0 - Encerrar o programa")

        print("Desejo a opção: ", end='')
        x = int(input())

        if x == 1:
            comprimento_de_onda()

        if x == 2:
            Freq()

        if x == 3:
            numero_onda()
        
        if x == 4:
            campo_Bm()

        if x == 5:
            campo_Em()

        if x == 0:
            break

main()
