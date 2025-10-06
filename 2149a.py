t = int(input())

for _ in range(t):
    mx = int(input())
    li = list(map(int, input().split()))
    res = 0
    ng = [n for n in li if n == -1]
    for x in li:
        if x == 0:
            res +=1
    if len(ng)%2 == 1:
        res+=2
    print(res)

