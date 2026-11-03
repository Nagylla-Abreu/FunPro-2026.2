print('UFC - Programação')
print('Nome: Nágylla Abreu')
conjunto = []
somatorio = 0
maior = 0

numelem = int(input('Número de Elementos do Conjunto: '))
for i in range(numelem):
    valor = float(input(f'Valor de Índice {i}: '))
    conjunto.append(valor)
    somatorio += valor
media = somatorio / numelem

for i in conjunto:
    if i > media:
        maior += 1

print(f'Elementos do Conjunto: {conjunto}')
print(f'\nValor da Média = {media:.2f}')
print(f'Quantidade Maior Que a Média = {maior}')
