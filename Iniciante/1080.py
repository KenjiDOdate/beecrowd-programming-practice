maxnum = 0 
posi = 0

for i in range(100):
    num = int(input())
    if num > maxnum:
        maxnum = num
        posi = i + 1


print(maxnum)
print(posi)