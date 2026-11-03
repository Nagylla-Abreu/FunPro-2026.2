lista = []
somatorio = 0
maior = 0
listamaior = []

numelem = int(input('Informe a quantidade de elemetntos da lista: '))

for i in range(numelem):
    valor = float(input(f'Digite o elemento [{i}] da Lista: '))
    lista.append(valor)
    somatorio += valor
    
media = somatorio / numelem
    
for i in lista:
    if i >= media:
        maior += 1
        listamaior.append(i)

print('\nUFC - Programação\n')
print(f'Valores da lista: {lista}')
print(f'Valor da Média = {media:.2f}')
print(f'Quantidade de elementos maiores/iguais a média = {maior}')
print(f'Elementos maiores/iguais a média: {listamaior}')
print('\nFim do Trabalho')
