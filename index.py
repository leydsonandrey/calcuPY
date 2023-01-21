import re
import sys


calculos_feitos = 0


def mostrar_contas_feitas():
    global calculos_feitos
    print(f"\nForam feitos: {calculos_feitos} calculos\n")


def sair():
    print("\nsaindo...\n")
    mostrar_contas_feitas()
    sys.exit()


def ajuda():
    print(
        '\ndigite "sair" para sair \n'
        'digite "ajuda" para ajuda \n'
    )


def calcular(value):
    try:
        if value == "":
            print("Erro: Calculo vazio")
        else:
            print(f'{eval(value)}')
            print()
    except SyntaxError:
        if re.findall("^0", value) == ['0']:
            print("Erro: Zero à esquerda não é permitido")
        else:
            # espaco_em_branco = re.split("\s", calculo)
            print("Erro: conta com varios calculos")
            # for i in re.split('\s', value):
            #     print(eval(i))


print("CALCUPY")

while True:
    try:
        calculo = input('> ')
        if calculo == "help":
            help()
        elif calculo == "quit":
            quit()
            break
        elif calculo.isalpha() or not "quit" or not "help":
            print("Erro: Letras não são permitidas")
        else:
            calcular(calculo)
    except KeyboardInterrupt:
        quit()
        break
