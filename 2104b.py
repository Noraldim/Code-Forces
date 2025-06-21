t = int(input())

for _ in range(t):
    ln = int(input())
    xm = list(map(int, input().split())) 
    xxm = xm[::-1]
    result = []
    if ln == 1:
        print(*xm)
        continue 
    if ln == 2:
        result.append(max(xm))
        result.append(sum(xm))
        print(*result)
        continue
    for index , x in enumerate(xxm):
        if index == 0:
            maxx = max(xxm)
            result.append(maxx)
            continue
        sub = xxm[0:index+1]
        el_sub = sub[-1] 
        bob = xxm[index+1:len(xxm)+1]
        bob_mx = max(bob) if bob else -1
        if bob_mx > el_sub:
            sub.pop()
            sub.append(bob_mx)
            fn = sum(sub)
            result.append(fn)
            continue
        else:
            fn = sum(sub)
            result.append(fn)
            continue


    print(*result)
