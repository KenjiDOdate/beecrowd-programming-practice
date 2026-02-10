renda = float(input())

imposto = 0.0

if renda <= 2000.00:
    print("Isento")
else:
    if renda > 4500.00:
        imposto += (renda - 4500.00) * 0.28
        renda = 4500.00

    if renda > 3000.00:
        imposto += (renda - 3000.00) * 0.18
        renda = 3000.00

    if renda > 2000.00:
        imposto += (renda - 2000.00) * 0.08

    print(f"R$ {imposto:.2f}")