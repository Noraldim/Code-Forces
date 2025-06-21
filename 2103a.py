t = int(input())
for _ in range(t):
    ln = int(input())
    mx = list(map(int, input().split()))
    cv = len(set(mx))
    print(cv)

