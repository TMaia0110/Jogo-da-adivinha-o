from time import sleep
from jogo import jogar






print('Qual o seu nome?')
nome = str(input('Digite aqui o seu nome: '))  # para fazer o usuário digitar o nome
sleep(0.7)
print(f'Olá, {nome}! Vamos jogar um jogo de adivinhação?')  # o F antes de aspas já formata tbm
sleep(0.5)
print('Sim (1)')  # dando opções para usuário
print('Não(2)')
resposta = str(input('Você aceita? '))
if resposta == '1':  # opção caso usuário aceite
    jogar(nome)
else:
    print('Ok. Até algum dia!')
