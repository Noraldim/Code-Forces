t = int(input())
for _ in range(t):
    mx = list(map(int, input().split()))
    n = mx[0]
    m = mx[1]
    p = mx[2]
    q = mx[3]
    if p == 1 and q != n/m:
        print("NO")
        continue
    if (n - p + 1) == m:
        print("YES")
        continue
    else:
        print("NO")
        continue
