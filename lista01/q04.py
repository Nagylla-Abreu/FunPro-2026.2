print("Programa para Gerar uma Sequência de M a N")
M = int(input("Digite o valor inical da sequência M: "))
N = int(input("Digite o valor inical da sequência N: "))
somatorio = 0
print("\nUFC - Programação")
print(f"Programa para Gerar uma Sequência de {M} a {N}")
print(f"Sequência: ")
for i in range(M, N+1):
    if i%2==0:
        somatorio+=i
    print(i, end=" ")
print(f"\nValor de M = {M}")
print(f"Valor de N = {N}")
print(f"Soma de todos os valores pares = {somatorio}")
