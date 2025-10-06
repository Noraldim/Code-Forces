t = int(input())

for _ in range(t):
    x , y = map(int, input().split())
    if y >  x :
        print(2)
        continue
    if y == x :
        print(-1)
        continue
    else:
        if x == y+1:
            print(-1)
            continue
        if y == 1 :
            print(-1)
            continue
        else :
            print(3)
            continue
