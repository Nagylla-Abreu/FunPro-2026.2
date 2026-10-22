print('UFC - Programação')
print('Programa para calcular a Média e Resultado do Aluno')

ap1 = float(input('Digite a primeira nota: '))
ap2 = float(input('Digite a segunda nota: '))
media = (ap1+ap2)/2

print('Curso: Engenharia de Computação')
print('Nome: Nágylla Abreu')

print(f'Primeira Avaliação = {ap1}')
print(f'Segunda Avaliação = {ap2}')
print(f'Média Parcial = {media}')
print('Resultado: ', end='')

if media >= 7:
    print('Aprovado')
elif 4<= media < 7:
    print(f'Prova Final')
else:
    print('Reprovado')
print('Fim do Trabalho')
