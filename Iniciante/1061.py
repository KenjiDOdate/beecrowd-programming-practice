_ , diasInicio = input().split()
diasInicio = int(diasInicio)
horasInicio, minutosInicio, segundosInicio = map(int, input().split(" : "))


_ , diasFim = input().split()
diasFim = int(diasFim)
horasFim, minutosFim, segundosFim = map(int, input().split(" : "))

inicio = (diasInicio * 24 * 60 * 60) + (horasInicio * 60 * 60) + (minutosInicio * 60) + segundosInicio
fim = (diasFim * 24 * 60 * 60) + (horasFim * 60 * 60) + (minutosFim * 60) + segundosFim

duracao = fim - inicio

dias = duracao // (24 * 60 * 60)
duracao = duracao % (24 * 60 * 60)

horas = duracao // (60 * 60)
duracao =  duracao % (60 * 60)

minutos = duracao // 60

segundos = duracao % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")