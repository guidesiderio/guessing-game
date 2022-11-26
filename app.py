import random

numero_randomico = random.randint(1, 100)
nome_jogador = input('Digite o nome do jogador: ')

palpite = int(input(f'{nome_jogador}, digite um palpite: '))

for i in range(4): # 5 palpites 

    if palpite == numero_randomico:
        print('Parabéns! Você acertou o número.\n')
    elif palpite > numero_randomico:
        print('Errou para cima... Tente um número maior.\n')
    else:
        print('Errou para baixo... Tente outro número.\n')    

    palpite = int(input(f'{nome_jogador}, digite outro palpite: '))

print('Parabéns! Você acertou o número.\n')