n = int(input())

for i in range(n):
    a, b, c = map(float, input().split())

    wa = ((a* 2) + (b * 3) + (c * 5))/ (2 + 3 + 5)
    print(f"{wa:.1f}")