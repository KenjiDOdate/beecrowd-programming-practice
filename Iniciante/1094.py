def percentual(tipo, total):
    calculo = (cobaias[tipo]/total) * 100
    print(f"Percentual de {tipoCobaia[tipo]}: {calculo:.2f} %")
    

n = int(input())

cobaias = {'C': 0, 'R': 0, 'S':0}
tipoCobaia = {'C': 'coelhos', 'R': 'ratos', 'S': 'sapos'}

for _ in range(n):
   qtd, tipo = input().split()
   cobaias[tipo] += int(qtd)

total = sum(cobaias.values())

print(f"Total: {total} cobaias")
for tipo in cobaias:
    print(f"Total de {tipoCobaia[tipo]}: {cobaias[tipo]}")


for tipo in cobaias:
    percentual(tipo, total)