numero_randomico = 31
nome_jogador = input('Digite o nome do jogador: ')
palpite = int(input(f'{nome_jogador}, digite o palpite: '))

if palpite == numero_randomico:
    print('Parabéns! Você acertou o número.')
else: 
    print('Erro! Você errou o número.')    