t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    prefix = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        prefix[n - i] = prefix[n - i - 1] + a[i]

    result = []
    max_elem = a[0]

    for k in range(1, n + 1):
        max_elem = max(max_elem, a[n - k])  # Best element to move into last k
        best_sum = prefix[k] - a[n - k] + max_elem
        result.append(best_sum)

    print(*result)

