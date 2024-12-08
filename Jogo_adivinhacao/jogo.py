from random import randint
from time import sleep

def jogar(nome):
    print('Ok. Vamos começar!')
    sleep(1.5)
    print(
        "O jogo funcionará assim: eu escolherei um número de 1-50 e você tentará adivinhar qual é o número. Você terá três tentativas. Boa sorte!")
    sleep(2)
    print('Escolhendo um número...')
    computador = randint(1, 50)  # para fazer o computador adivinhar
    sleep(1)
    print('Pronto! Número escolhido! Agora é a sua vez!')
    tentativas = 0
    while tentativas < 3:
        numero_escolhido = int(
            input('Tentativa {}. Digite um número: '.format(tentativas + 1)))  # jogador tenta adivinhar
        if numero_escolhido <= 0 or numero_escolhido > 50:  # valida se o número está dentro do range
            print('Número invalido! Tente um número de 1 a 50')
        else:
            tentativas = tentativas + 1
            print('PROCESSANDO...')
            if numero_escolhido == computador:
                print('Parabéns!! Você acertou o número!! Muito bom 06!!')
                break
            elif tentativas == 3:
                print(f'Sinto muito {nome}, acabaram suas tentativas :(')
            elif numero_escolhido < computador:
                print('Ops... Parece que você chutou baixo demais... Tente um número maior.')
            elif numero_escolhido > computador:
                print('Eitaaaa... Parece que você chutou alto demais! Tente um número mais baixo.')