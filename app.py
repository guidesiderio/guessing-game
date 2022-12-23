import random
import time

# Menu de opções
def menu_regras():
    print('\nRegras do nível de jogo:')
    print('"F" - Nível 1 (fácil): acerte em até 10 jogadas.')
    print('"M" - Nível 2 (médio): acerte em até 5 jogadas.')
    print('"D" - Nível 3 (difícil): acerte em até 3 jogadas.\n')

# Função que retorna um valor booleano de acordo com a escolha do jogador
def jogar_novamente(resp):
    resp = False
    while True:
        print(f'{nome_jogador}, você deseja jogar novamente?')
        ler_resposta = input('S - Sim ou N - Não: ').upper()
        if ler_resposta == 'S':
            resp = True
            break
        elif ler_resposta == 'N':
            resp = False
            break
        else:
            print('Opção Inválida!\n')

    return resp     

# Função que retorna um número de tentativas de acordo com o nível do jogo
def nivel_jogo():
    tentativas = 0
    while True:
        menu_regras()
        nivel = input('Digite o nível do jogo: ').upper()
        if nivel == 'F':
            tentativas = 10
            break
        elif nivel == 'M':
            tentativas == 5
            break
        elif nivel == 'D':
            tentativas = 3
            break
        else:
            print('Nível inválido!\n')

    return tentativas        

# Gera um número inteiro aletatório entre 0 e 100
numero_randomico = random.randint(0, 100)

# Aplicação
print('--- Bem vindo ao Jogo de Adivinhação! ---')

nome_jogador = input('Digite o nome do jogador: ')

resposta = True
while resposta:

    tentativas = nivel_jogo()

    start = time.perf_counter() # Tempo inicial

    tentativas_falhas = 0
    for i in range(tentativas): # Limite máximo de tentativas
        
        palpite = input(f'{nome_jogador}, qual o seu palpite?: ')
        palpite_usuario = int(palpite)

        if palpite_usuario == numero_randomico:
            print(f'Parabéns {nome_jogador}! Você acertou o número secreto em {tentativas_falhas} tentativas!')
            break
        elif palpite_usuario > numero_randomico:
            tentativas_falhas += 1
            print(f'\nTentativa nº{tentativas_falhas}.')
            print('Errou para cima... Tente um número menor.\n')
        else:
            tentativas_falhas += 1
            print(f'\nTentativa nº{tentativas_falhas}.')
            print('Errou para baixo... Tente outro número maior.\n')

    end = time.perf_counter() # Tempo Final

    if tentativas_falhas == tentativas:
        print('Game Over! Você utilizou todas as tentativas.')

    elapsed = end - start
    print(f'Duração: {elapsed:.2f} segundos\n')
    
    resp = jogar_novamente(resposta)
    resposta = resp

print('\nFim de jogo!\n')
           