import re
import comandos

def calcular(value):
    try:
        if value == "":
            print("Erro: Calculo vazio")
        else:
            print('\n', eval(value), '\n')
            comandos.contas_feitas()
    except SyntaxError:
        if re.findall("^0", value) == ['0']:
            print("\nErro: Zero à esquerda não é permitido\n")
        else:
            # espaco_em_branco = re.split("\s", calculo)
            print("\nErro: conta com varios calculos\n")
            # for i in re.split('\s', value):
            #     print(eval(i))


print("CALCUPY")

while True:
    try:
        calculo = input('> ')

        if calculo == "ajuda" or re.findall("ajuda", calculo) == ['ajuda']:
            comandos.ajuda()
        elif calculo == "sair" or re.findall("sair", calculo) == ['sair']:
            comandos.sair()
        elif calculo == "contas" or re.findall("contas", calculo) == ['contas']:
            comandos.mostrar_contas_feitas()
        elif calculo.isalpha():
            print("\nErro: Letras não são permitidas\n")
        else:
            calcular(calculo)

    except KeyboardInterrupt:
        comandos.sair()
