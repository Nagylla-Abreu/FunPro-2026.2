from math import sqrt

print("UFC - Programação")
print("Cálculo das Raízes de uma Equação do Segundo Grau\n")

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

print(f"\nValor de Delta = {delta}")

if delta > 0:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print(f"Valor de x1 = {x1}")
    print(f"Valor de x2 = {x2}")
elif delta == 0:
    x1 = -b / (2 * a)
    print(f"Valor de x1 = {x1}")
else:
    print("Não tem raízes nos reais.")
