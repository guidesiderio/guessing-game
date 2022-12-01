import random

numero_randomico = random.randint(1, 100)
nome_jogador = input('Digite o nome do jogador: ')

print('\nRegras do nível de jogo:')
print('1- Nível 1 (fácil): acerte em menos de 10 jogadas')
print('2- Nível 2 (médio): acerte em menos de 5 jogadas')
print('3- Nível 3 (difícil): acerte em menos de 3 jogadas\n')

tentativas = 0
while True:
    nivel = int(input('Digite o nível do jogo: '))
    nivel_jogo = int(nivel)

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

tentativas_falhas = 0
for i in range(tentativas):
    palpite = input(f'{nome_jogador}, qual o seu palpite?: ')
    palpite_usuario = int(palpite)

    if palpite_usuario == numero_randomico:
        print('Parabéns! Você acertou o número.\n')
        break
    elif palpite_usuario > numero_randomico:
        print('Errou para cima... Tente um número menor.\n')
        tentativas_falhas += 1
    else:
        print('Errou para baixo... Tente outro número maior.\n')
        tentativas_falhas += 1

if tentativas_falhas == tentativas:
    print('Game Over! Você utilizou todas as tentativas.\n')
           