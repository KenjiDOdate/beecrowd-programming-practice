begin, final = map(int, input().split())

if begin == final:
    print("O JOGO DUROU 24 HORA(S)")
elif begin < final:
    print(f"O JOGO DUROU {final - begin} HORA(S)")
else:
    alfa = 24 - begin
    hours = alfa + final
    print(f"O JOGO DUROU {hours} HORA(S)")