def main():
    calculos_feitos = 0


    def quit(feitos):
        print(f'foram feitos {feitos} calculos')
        print("saindo...")


    def help():
        print('digite "quit" para sair\ndigite "help" para ajuda')


    def calcular(calculo):
        try:
            print(f'{eval(calculo)}')
            print()
        except Exception: # as e:
            if calculo == "":
                return print("Erro: Calculo vazio")
            else: 
                return print(f'Erro: Calculo escrito errado') # :  {str(e)}')


    print("CALCUPY")

    while True:
        calculo = input('> ')
        if calculo == "quit":
            quit(calculos_feitos)
            break
        elif calculo == "help":
            help()
        elif calculo.isalpha() or not "quit" or not "help":
            print("| Letras não são permitidas")
        else:
            calcular(calculo)
            calculos_feitos += 1

if __name__ == '__main__':
    main()
