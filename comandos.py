import sys


calculos_feitos = 0


def contas_feitas():
    global calculos_feitos
    calculos_feitos += 1


def mostrar_contas_feitas():
    global calculos_feitos
    print(f"\nForam feitos: {calculos_feitos} calculos\n")


def sair():
    mostrar_contas_feitas()
    print("saindo...\n")
    sys.exit()


def ajuda():
    print(
        '\ndigite "sair" para sair \n'
        'digite "ajuda" para ajuda \n'
        'digite "contas" para ver a quantidade de contas feitasn \n'
    )




