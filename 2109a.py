t = int(input())
for _ in range(t):
    ln = int(input())
    mx = list(map(int , input().split()))
    one  = 0
    zero  = 0 
    for index ,  x in enumerate(mx):
        if x == 1:
            one+=1
        if x == 0:
            zero+=1
            if index != 0 and mx[index] == mx[index-1]:
                print("YES")
                break
    if one == ln or zero == ln :
        print("YES")
        continue
    ck = int(ln/2)
    if one == ck +1 or one == ck:
        print("NO")
        continue
