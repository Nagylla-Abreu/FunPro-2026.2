print('UFC - Programação')
print('Nome: Nágylla Abreu')
print('Programa para Calcular o Valor de F\n')

K = int(input('Insira o valor de K: '))
L = int(input('Insira o valor de L: '))
F = 0


for i in range (1, L+1):
    F += (K**i)/i

print(f'\nValor da função F = {F:.2f}')
print(f'Valor de K = {K}')
print(f'Valor de L = {L}')
