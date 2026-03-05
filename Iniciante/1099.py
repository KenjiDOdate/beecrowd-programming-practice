def somarImpares(a, b):

    inicio = min(a, b)
    fim = max(a, b)
    soma = 0

    for i in range(inicio + 1, fim):
        if i % 2 != 0:
            soma += i

    print(soma)

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    somarImpares(a, b)

