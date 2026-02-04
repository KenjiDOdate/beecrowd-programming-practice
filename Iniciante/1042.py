valores = [int(x) for x in input().split()]

valorescrescentes = valores.copy()

n = 0
for j in range(len(valorescrescentes)):
    for i in range(len(valorescrescentes) - 1):
        if valorescrescentes[i] > valorescrescentes[i+1]:
            valorescrescentes[i], valorescrescentes[i +
                                                    1] = valorescrescentes[i+1], valorescrescentes[i]

for o in range(len(valorescrescentes)):
    print(valorescrescentes[o])

print()

for p in range(len(valores)):
    print(valores[p])
