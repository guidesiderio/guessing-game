import random

numero_randomico = random.randint(1, 100)
nome_jogador = input('Digite o nome do jogador: ')

print('Regras do nível de jogo:')
print('1- Nível 1 (fácil): acerte em menos de 10 jogadas')
print('2- Nível 2 (médio): acerte em menos de 5 jogadas')
print('3- Nível 3 (difícil): acerte em menos de 3 jogadas')
nivel_jogo = int(input('Digite o nível do jogo: '))

palpite = int(input(f'{nome_jogador}, digite um palpite: '))

for i in range(nivel_jogo):

    if palpite == numero_randomico:
        print('Parabéns! Você acertou o número.\n')
    elif palpite > numero_randomico:
        print('Errou para cima... Tente um número menor.\n')
    else:
        print('Errou para baixo... Tente outro número maior.\n')    

    palpite = int(input(f'{nome_jogador}, digite outro palpite: '))

print('Parabéns! Você acertou o número.\n')