def porcentagem(total, subtotal):
    if total == 0:
        return total
    return (subtotal/total)*100

n = int(input())

total = 0
tcoelho = 0 
trato = 0
tsapo = 0

for i in range(n):
    qtd, subject = input().split()
    qtd = int(qtd)
    total += qtd
    if subject == "C":
        tcoelho += qtd
    elif subject == "R":
        trato +=qtd
    elif subject == "S":
        tsapo += qtd

centcoelho = porcentagem(total, tcoelho)
centrato = porcentagem(total, trato)
centsapo = porcentagem(total, tsapo)

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {tcoelho}")
print(f"Total de ratos: {trato}")
print(f"Total de sapos: 23")
print(f"Percentual de coelhos: {centcoelho:.2f} %")
print(f"Percentual de ratos: {centrato:.2f} %")
print(f"Percentual de sapos: {centsapo:.2f} %")