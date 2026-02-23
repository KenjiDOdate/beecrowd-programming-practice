a = int(input())
b = int(input())

inicio = min(a, b)
fim = max(a, b)
soma = 0

for i in range(inicio + 1, fim):
    if i % 2 != 0:
        soma += i

print(soma)
