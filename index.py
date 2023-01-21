import re


def quit():
    print("saindo...")


def help():
    print(
        'digite "quit" para sair \n'
        'digite "help" para ajuda \n'
        'digite "calculos" para ver a quantidade de calculos feitos'
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
            for i in re.split("\s", value):
                print(eval(i))


print("CALCUPY")

while True:
    try:
        calculo = input('> ')
        if calculo == "quit":
            quit()
            break
        elif calculo == "help":
            help()
        elif calculo.isalpha() or not "quit" or not "help":
            print("Erro: Letras não são permitidas")
        else:
            calcular(calculo)
    except KeyboardInterrupt:
        quit()
        break
