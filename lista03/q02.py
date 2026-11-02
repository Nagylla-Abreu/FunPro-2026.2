lista = []
somatorio = 0

for i in range(10):
    valor = int(input(f'Digite Vr da Lista Índice[{i}]: '))
    lista.append(valor)
    somatorio += valor
  
media = somatorio / 10

print('\nUFC - Programação')
print(f'\nValores da Lista: {lista}')
print(f'\nMédia = {media}')
print('\nFim do Trabalho')
