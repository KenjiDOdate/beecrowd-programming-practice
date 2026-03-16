def somar(m, n):
    numbers = []
    inicio = min(m, n)
    fim = max(m, n)
    soma = 0

    for i in range(inicio, fim+1):
            soma += i
            numbers.append(i)

    print(f'{" ".join(map(str, numbers))} Sum={soma}')


while True:
    m, n = map(int, input().split())
    if  m <= 0 or n <= 0:
        break
    somar(m,n)