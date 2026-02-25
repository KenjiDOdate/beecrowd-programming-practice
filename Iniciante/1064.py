numPositivo = 0
soma = 0
for i in range(6):
    num = float(input())
    if num > 0:
        numPositivo += 1
        soma += num

media = soma / numPositivo

print(f"{numPositivo} valores positivos")
print(f"{media:.1f}")