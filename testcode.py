for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    x = set(a) - {0}
    y = sorted(set(range(1, n+1)) - x)
    k = 0
    for i in range(n):
        if a[i] == 0:
            a[i] = y[-1-k]
            k += 1

    l, r = 0, n-1
    while l < n and a[l] == l+1:
        l += 1
    while r >= 0 and a[r] == r+1:
        r -= 1
    res = max(0, r-l+1)
    print(res)

