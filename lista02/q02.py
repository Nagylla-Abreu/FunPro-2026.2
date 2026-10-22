print('UFC - Programação')

pares = 0
impares = 0
qtdpar = 0
qtdimpar = 0
somatorio = 0

M = int(input('Insira o valor inical M: '))
N = int(input('Insira o valor final N: '))

print('Valores da Sequência')
for i in range(M, N+1):
    print(f'{i}', end=' ')
    if i % 2 == 0:
        pares = pares + i
        qtdpar += 1
    else:
        impares = impares + i
        qtdimpar += 1
    somatorio += i
mpar = pares/qtdpar
mimpar = impares/qtdimpar

print(f'\nValor de M = {M}')
print(f'Valor de N = {N}')
print(f'Média dos Valores Pares = {mpar}')
print(f'Média dos Valores Impares = {mimpar}')
print(f'Somatório = {somatorio}')

print('\nFim do Trabalho')
