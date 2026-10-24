print('UFC - Programação')
print('Nome: Nágylla Abreu')
N = int(input('Insira o valor de N: '))
Fat = 1
for i in range(N, 0, -1):
    Fat = Fat * i
print(f'Resultado fatorial: {Fat}')
print(f'Valor de N = {N}')
