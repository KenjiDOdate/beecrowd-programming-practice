def resultado(salario, percentual):

    salarionovo = salario + (salario * (percentual/100))     
    reajuste = salario * (percentual/100)

    print(f"Novo salario: {salarionovo:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual} %")


salario = float(input())

if salario <= 400:
    resultado(salario, 15)
elif 400 < salario <=800:
    resultado(salario, 12)
elif 800 < salario <= 1200:
    resultado(salario, 10)
elif 1200 < salario <= 2000:
    resultado(salario, 7)
else:
    resultado(salario, 4)
