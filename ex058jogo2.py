print('\n========== DESAFIO 58 ==========')
from random import randint
computador = randint(0, 10)
jogador = 11
cont = 0

print('\n================= João da Adivinhação =================')
print('Tente acertar em qual número, entre 0 e 10, eu pensei')
print('=======================================================)')

while jogador != computador:
    jogador = int(input('Qual seu palpite? '))
    cont += 1
    if jogador < computador:
        print('Errou! É maior')
    if jogador > computador:
        print('Errou! É menor')
print(f'NA MOSCA! Você precisou de {cont} palpites para certar') 
    