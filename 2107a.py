for _ in range(int(input())):
    n = int(input())
    xm = list(map(int , input().split()))

    if len(set(xm)) == 1:
        print("NO")
    else:
        print("yes")
        x = xm.index(max(xm))
        answer = [1] * n 
        answer[x] = 2
        print(*answer)


