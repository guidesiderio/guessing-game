import random

numero_randomico = random.randint(1, 100)
nome_jogador = input('Digite o nome do jogador: ')

palpite = int(input(f'{nome_jogador}, digite um palpite: '))

while palpite != numero_randomico:
        print('Erro! Você errou o número.\n')
        palpite = int(input(f'{nome_jogador}, digite outro palpite: '))

print('Parabéns! Você acertou o número.\n')