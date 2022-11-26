import random

numero_randomico = random.randint(1, 100)
nome_jogador = input('Digite o nome do jogador: ')

print('\nRegras do nível de jogo:')
print('1- Nível 1 (fácil): acerte em menos de 10 jogadas')
print('2- Nível 2 (médio): acerte em menos de 5 jogadas')
print('3- Nível 3 (difícil): acerte em menos de 3 jogadas\n')

tentativas = 0
while True:
    nivel_jogo = int(input('Digite o nível do jogo: '))

    if nivel_jogo == 1:
        tentativas = 10
        break
    elif nivel_jogo == 2:
        tentativas == 5
        break
    elif nivel_jogo == 3:
        tentativas = 3
        break
    else:
        print('Nível inválido!\n')

for i in range(tentativas):
    palpite = int(input(f'{nome_jogador}, qual o seu palpite?: '))

    if palpite == numero_randomico:
        print('Parabéns! Você acertou o número.\n')
        break
    elif palpite > numero_randomico:
        print('Errou para cima... Tente um número menor.\n')
    else:
        print('Errou para baixo... Tente outro número maior.\n')
    

        